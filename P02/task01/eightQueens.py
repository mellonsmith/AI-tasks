class EightQueens:

    def __init__(self, initial_state=None, transition_model=None):
        self.initial_state = initial_state or [0, 1, 2, 3, 4, 5, 6, 7]
        self.transition_model = transition_model or self.default_transition_model
        self.cost_function = self.default_cost_function
        self.heuristic_function = self.default_heuristic_function

    def default_transition_model(self, state):
        successors = []
        for col in range(8):
            for row in range(8):
                if self.is_valid(row, col):
                    new_state = state.copy()
                    new_state[col] = row
                    successors.append(new_state)
        return successors

    def is_valid(self, row, col):
        for i in range(col):
            # Überprüfe, ob Dame in der gleichen Zeile oder Diagonale
            if self.solution[i] == row or \
               self.solution[i] - row == i - col or \
               self.solution[i] - row == col - i or \
               col == i:
                return False
        return True

    def default_cost_function(self, state):
        conflicts = 0
        for i in range(8):
            for j in range(i+1, 8):
                if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                    conflicts += 1
        return conflicts

    def default_heuristic_function(self, state):
        return self.default_cost_function(state)

    def visualize_state(self, state):
        board = []
        for i in range(8):
            row = ["_" for _ in range(8)]
            row[state[i]] = "Q"
            board.append(" ".join(row))
        return "\n".join(board)

    def visualize_cost(self, state):
        return str(self.cost_function(state))
