import eightQueens as EightQueens


class EightQueensBacktracking:
    def __init__(self):
        self.board_size = 8
        self.solution = [None] * self.board_size
        self.eq = EightQueens.EightQueens()

    def solve(self):
        if self.backtrack(0):
            return self.solution
        else:
            return None

    def backtrack(self, col):
        if col == self.board_size:
            return True

        for row in range(self.board_size):
            if self.is_valid(row, col):
                self.solution[col] = row

                if self.backtrack(col + 1):
                    return True

                self.solution[col] = None

        return False

    def is_valid(self, row, col):
        for i in range(col):
            # Überprüfe, ob Dame in der gleichen Reihe, Zeile oder Diagonale
            if self.solution[i] == row or \
               self.solution[i] - row == i - col or \
               self.solution[i] - row == col - i or\
               col == i:
                return False
        return True


# Beispielanwendung
backtracking = EightQueensBacktracking()
solution = backtracking.solve()

if solution is not None:
    print("Lösung gefunden:")
    print(backtracking.eq.visualize_state(solution))
else:
    print("Keine Lösung gefunden.")
