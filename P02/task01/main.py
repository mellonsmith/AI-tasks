from eightQueens import *


# Create an instance of the class with a specific initial state
problem = EightQueens(initial_state=[4, 2, 0, 6, 1, 7, 5, 3])

# Generate all successor states of the initial state using the default transition model
successors = list(problem.transition_model(problem.initial_state))

# Visualize the initial state and its heuristic and cost values
print(problem.visualize_state(problem.initial_state))
print("Heuristic value:", problem.heuristic_function(problem.initial_state))
print("Cost value:", problem.cost_function(problem.initial_state))

# Visualize some successor states and their heuristic and cost values
for successor in successors[:3]:
    print(problem.visualize_state(successor))
    print("Heuristic value:", problem.heuristic_function(successor))
    print("Cost value:", problem.cost_function(successor))
