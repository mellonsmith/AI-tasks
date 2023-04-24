from graph import *
from utils import *
from prettytable import PrettyTable


romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
 'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
 'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
[
   ('Or', 'Ze', 71), ('Or', 'Si', 151),
   ('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
   ('Ia', 'Va', 92), ('Ar', 'Si', 140),
   ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
   ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
   ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
   ('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
   ('Lu', 'Me', 70), ('Me', 'Dr', 75),
   ('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
   ('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
   ('Bu', 'Ur', 85), ('Ur', 'Hi', 98),
   ('Hi', 'Ef', 86)
] )

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def fifo(self):
        return self.items[-1]
    def lifo(self):
        return self.items[0]
    def priority(self):
        return self.items[0]
    


def breadth_first_search(graph, start, goal):    
    frontier = Queue()
    frontier.enqueue(start)
    came_from = {}
    came_from[start] = None

    while not frontier.isEmpty():
        current = frontier.fifo()
        if current == goal:
            break
        for next in frontier.edges:
            if next not in came_from:
                frontier.enqueue(next)
                came_from[next] = current
    return came_from

def depth_first_search(graph, start, goal):
    frontier = Queue()
    frontier.enqueue(start)
    came_from = {}
    came_from[start] = None

    while not frontier.isEmpty():
        current = frontier.lifo()
        if current == goal:
            break
        for next in frontier.edges:
            if next not in came_from:
                frontier.enqueue(next)
                came_from[next] = current
    return came_from

def uniform_cost_search(graph, start, goal):
    frontier = Queue()
    frontier.enqueue(start)
    came_from = {}
    came_from[start] = None

    while not frontier.isEmpty():
        current = frontier.priority()
        if current == goal:
            break
        for next in frontier.edges:
            if next not in came_from:
                frontier.enqueue(next)
                came_from[next] = current
    return came_from

print("Breadth First Search: " + breadth_first_search(romania, 'Or', 'Bu'))
print("Depth First Search: " + depth_first_search(romania, 'Or', 'Bu'))
print("Uniform Cost Search: " + uniform_cost_search(romania, 'Or', 'Bu'))
