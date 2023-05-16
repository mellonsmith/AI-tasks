class EightQueensBacktracking:
    def __init__(self):
        self.solutions = []

    def solve_eight_queens_backtracking(self):
        board = [[0 for _ in range(8)] for _ in range(8)]
        self.backtrack(board, 0)
        self.print_solutions()

    def backtrack(self, board, row):
        if row == 8:
            self.save_solution(board)
            return

        for col in range(8):
            if self.is_valid_position(board, row, col):
                board[row][col] = 1
                self.backtrack(board, row + 1)
                board[row][col] = 0

    def is_valid_position(self, board, row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False

            if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
                return False

            if col + (row - i) < 8 and board[i][col + (row - i)] == 1:
                return False

        return True

    def save_solution(self, board):
        solution = []
        for row in range(8):
            for col in range(8):
                if board[row][col] == 1:
                    solution.append(col + 1)
        self.solutions.append(solution)

    def print_solutions(self):
        for i, solution in enumerate(self.solutions):
            print(f"Solution {i + 1}: {solution}")


if __name__ == '__main__':
    backtracking = EightQueensBacktracking()
    backtracking.solve_eight_queens_backtracking()
