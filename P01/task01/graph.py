from prettytable import PrettyTable
from utils import *
import heapq


class Node:

    def __init__(self, name):
        self.parent = 0
        self.name = name
        self.edges = []
        self.value = 0


class Edge:

    def __init__(self, edge):
        self.start = edge[0]
        self.end = edge[1]
        self.value = edge[2]


class Graph:

    def __init__(self, node_list, edges):
        self.nodes = []
        for name in node_list:
            self.nodes.append(Node(name))

        for e in edges:
            e = (getNode(e[0], self.nodes), getNode(e[1], self.nodes), e[2])

            self.nodes[next((i for i, v in enumerate(self.nodes)
                            if v.name == e[0].name), -1)].edges.append(Edge(e))
            self.nodes[next((i for i, v in enumerate(
                self.nodes) if v.name == e[1].name), -1)].edges.append(Edge((e[1], e[0], e[2])))

    def print(self):
        node_list = self.nodes

        t = PrettyTable(['  '] + [i.name for i in node_list])
        for node in node_list:
            edge_values = ['X'] * len(node_list)
            for edge in node.edges:
                edge_values[next((i for i, e in enumerate(
                    node_list) if e.name == edge.end.name), -1)] = edge.value
            t.add_row([node.name] + edge_values)
        print(t)


romania = Graph(['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
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
])


class Queue:
    def __init__(self, edges):
        self.items = []

    def is_empty(self):  # Methode hinzugefügt
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def fifo(self):
        return self.items[-1]

    def lifo(self):
        return self.items[0]

    def prio(self):
        if self.isEmpty():  # Ändere "is_empty" zu "isEmpty"
            return None
        min_index = 0
        for i in range(1, len(self.items)):
            if self.items[i][0] < self.items[min_index][0]:
                min_index = i
        return self.items.pop(min_index)

    def enqueue_with_priority(self, item, priority):
        self.items.append((priority, item))

    def dequeue_with_priority(self):
        if self.is_empty():
            return None
        min_priority = float('inf')
        min_index = 0
        for i, (priority, _) in enumerate(self.items):
            if priority < min_priority:
                min_priority = priority
                min_index = i
        return self.items.pop(min_index)[1]


def breadth_first_search(graph, start, end):
    queue = Queue([])
    queue.enqueue([start])
    while queue:
        path = queue.dequeue()
        node = path[-1]
        if node == end:
            return path
        for edge in graph.nodes[next((i for i, v in enumerate(graph.nodes) if v.name == node), -1)].edges:
            new_path = list(path)
            new_path.append(edge.end.name)
            queue.enqueue(new_path)
    return None


def depth_first_search(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    if start == end:
        return path

    visited.add(start)
    for edge in graph.nodes[next((i for i, v in enumerate(graph.nodes) if v.name == start), -1)].edges:
        if edge.end.name not in visited:
            new_path = path + [edge.end.name]
            result = depth_first_search(
                graph, edge.end.name, end, visited, new_path)
            if result is not None:
                return result

    return None


def uniform_cost_search(graph, start, end):
    queue = Queue([])
    # Verwende enqueue_with_priority-Methode
    queue.enqueue_with_priority([start], 0)

    while not queue.is_empty():
        path = queue.dequeue_with_priority()
        node = path[-1]
        if node == end:
            return path
        # gehe durch die Kanten des Knotens und füge die Kosten hinzu
        for edge in graph.nodes[next((i for i, v in enumerate(graph.nodes) if v.name == node), -1)].edges:
            new_cost = path_cost(path, graph) + edge.value
            new_path = list(path)
            new_path.append(edge.end.name)
            queue.enqueue_with_priority(new_path, new_cost)

    return None


def path_cost(path, graph):
    cost = 0
    current_node = graph.nodes[next(
        (i for i, v in enumerate(graph.nodes) if v.name == path[0]), -1)]
    for next_node_name in path[1:]:
        for edge in current_node.edges:
            if edge.end.name == next_node_name:
                cost += edge.value
                current_node = edge.end
                break
    return cost
