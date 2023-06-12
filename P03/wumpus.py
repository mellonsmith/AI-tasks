# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:12:35 2023

@author: Luis,Jonathan
"""

import gym
import fh_ac_ai_gym
from collections import defaultdict

# WALK = 0
# TURNLEFT = 1
# TURNRIGHT = 2
# GRAB = 3
# SHOOT = 4
# CLIMB = 5

class Wumpus:
    
    def __init__(self):
        self.KB = {"clauses":[],"symbols":[]}
        
        self.count ={} # number of symbols in clause's premise
        self.inferred = defaultdict(lambda: False)
        self.wumpus_env = gym.make('Wumpus-v0')
        self.cartpole_env = gym.make('Fuzzy-CartPole-v0')
        self.wumpus_env.reset()
        self.populateKB()
        
        #the starting field is always safe
        self.KB['symbols'].append("OK11")
    
    #Populate the KB
    def populateKB(self):
        """
        Populate the KB by applying game rules:
            1. Fields that are OK have neither pit nor wumpus
            2. If there is a stench or breeze there has to be a pit or wumpus
                at one of the adjacent fields

        Returns
        -------
        None.

        """
        
        fieldEventPairs =[['B','P'],['S','W']]
        for x in range(1,5):
            for y in range(1,5):
                # #the starting field is safe
                # if not x == 1 and y == 1: 
                #     # Positive Clauses
                #     # "Circle" all the pits, golds, and wumpus 
                #     for pair in fieldEventPairs:
                #         clause = ""
                #         if x+1 < 5:
                #             clause += f"{pair[0]}{x+1}{y},"
                #         if x-1 > 0:
                #             clause += f"{pair[0]}{x-1}{y},"
                #         if y+1 < 5:
                #             clause += f"{pair[0]}{x}{y+1},"
                #         if y-1 > 0:
                #             clause += f"{pair[0]}{x}{y-1},"
                #         clause = clause.strip(',')
                #         clause += f"=>{pair[1]}{x}{y}"
                #         self.KB['clauses'].append(clause)
                        
                # if a field is okay there can be no pit and no wumpus
                clause = f"OK{x}{y}=>-P{x}{y}"
                self.KB['clauses'].append(clause)
                clause = f"OK{x}{y}=>-W{x}{y}"
                self.KB['clauses'].append(clause)
                
                
                
                # deduce if there is a pit or wumpus by combining visited field
                # and perception
                # x direction
                for pair in fieldEventPairs:
                    clause = f"{pair[0]}{x}{y},"
                    if x + 1 < 5:
                        if x-1>0:
                            clause+=f"-{pair[1]}{x-1}{y},"
                        if y-1>0:
                            clause+=f"-{pair[1]}{x}{y-1},"
                        if y+1<5:
                            clause+=f"-{pair[1]}{x}{y+1},"
                        clause = clause.strip(',')
                        clause += f"=>{pair[1]}{x+1}{y}"
                        self.KB['clauses'].append(clause)  
                        
                    clause = f"{pair[0]}{x}{y},"
                    if x - 1 > 5:
                        if x+1<5:
                            clause+=f"-{pair[1]}{x+1}{y},"
                        if y-1>0:
                            clause+=f"-{pair[1]}{x}{y-1},"
                        if y+1<5:
                            clause+=f"-{pair[1]}{x}{y+1},"
                        clause = clause.strip(',')
                        clause += f"=>{pair[1]}{x-1}{y}"
                        self.KB['clauses'].append(clause) 
                    
                    # y direction
                    clause = f"{pair[0]}{x}{y},"
                    if y + 1 < 5:
                        if x-1>0:
                            clause+=f"-{pair[1]}{x-1}{y},"
                        if x+1<5:
                            clause+=f"-{pair[1]}{x+1}{y},"
                        if y-1>0:
                            clause+=f"-{pair[1]}{x}{y-1},"
                        clause = clause.strip(',')
                        clause += f"=>{pair[1]}{x}{y+1}"
                        self.KB['clauses'].append(clause) 
                        
                    clause = f"{pair[0]}{x}{y},"
                    if y - 1 > 0:
                        if x-1>0:
                            clause+=f"-{pair[1]}{x-1}{y},"
                        if x+1<5:
                            clause+=f"-{pair[1]}{x+1}{y},"
                        if y+1<5:
                            clause+=f"-{pair[1]}{x}{y+1},"
                        clause = clause.strip(',')
                        clause += f"=>{pair[1]}{x}{y-1}"
                        self.KB['clauses'].append(clause) 
            
    def TELL(self, percept: dict):
        """
        Converts a perception sequence into valid symbols e.g. -S33 or B23
        
        Parameters
        ----------
        percept : dict
            perception sequence
        """
        events = ['stench','breeze','glitter']
        eventdict = {'stench':'S', 'breeze':'B', 'glitter':'Gl'}
        for event in events:
            minus = ""
            if not percept[event]: minus = "-"
            newSymbol = f"{minus}{eventdict[event]}{percept['x']+1}{percept['y']+1}"
            if not newSymbol in self.KB['symbols']:
                self.KB['symbols'].append(newSymbol)
        # Visited fields are safe
        newSymbol = f"OK{percept['x']+1}{percept['y']+1}"
        if not newSymbol in self.KB['symbols']:
            self.KB['symbols'].append(newSymbol)
    
    def PLFCEntails(self, q: str)-> bool:
        """
        Checks if KB|=q by forward chaining
        
        Parameters
        ----------
        q : str
            query, proposition symbol
    
        Returns
        -------
        bool
            KB|=q ?
    
        """
        # populate count and add true symbols to agenda
        for clause in self.KB["clauses"]:
            self.populateCount(clause)
        
        print(f"Symbols: {self.KB['symbols']}")
        agenda = list(self.KB["symbols"]) # shallow copy
        #print(f"Count: {self.count}")
        #print(f"KB Clauses:")
        #for clause in self.KB['clauses']:
        #    print(clause)
        while(len(agenda) > 0):
            s = agenda.pop() # s (symbol) instead of p for clarity
            if s == q: 
                return True
            if(not self.inferred[s]):
                self.inferred[s] = True
            clausesWithS = [c for c in self.KB['clauses'] if self.symbolInClause(s, c)]
            for c in clausesWithS:
                self.count[c] -= 1
                if(self.count[c] == 0):
                    conclusion = c.split('=>')[1]
                    agenda.append(conclusion)
        return False
                
    def symbolInClause(self, symbol: str, c: str)->bool:
        """
        Checks whether a symbol is in a clause premise
        """
        p = c.split('=>')
        p = p[0].split(',')
        return symbol in p
    
    def populateCount(self, c: str):
        """Counts the number of symbols in the premise of a clause and stores it 
        in a dict.
        
        Parameters:
            c (str): Clause
            """
        premise = c.split('=>')[0]
        self.count[c] = len(premise.split(','))
    
    def ASK(self, q: str):
        not_there = ""
        if not self.PLFCEntails(q): not_there = "not "
        print("__________________________________")
        print(f"{q} is {not_there}entailed by the KB")
        print("__________________________________")
    
    def step(self, action: int):
        percept = self.wumpus_env.step(action)
        self.wumpus_env.render()
        # Check loss condition
        if percept[1][0] <= -1000:
            print("You died")
            return
        self.TELL(percept[0])
        
w = Wumpus()


def check():
    w.step(1)
    w.ASK('W21')
    w.ASK('P23')
    w.step(0)
    w.ASK('W21')
    w.ASK('P23')
    w.step(0)
    w.ASK('P23')
    w.step(0)
    w.ASK('P23')
    w.step(2)
    w.ASK('P23')
    w.step(0)
    w.ASK('P23')
    w.step(0)
    w.ASK('P23')
    
check()


