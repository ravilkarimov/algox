'''
Backtrack algo as example for N-Qeens problem:

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other. Given an integer n, return all
distinct solutions to the n-queens puzzle. You may return the answer in any
order. Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space,
respectively.
'''


class NQueens:
    def solve(self, n: int) -> list[list[str]]:
        board = [[False] * n for _ in range(n)]
        rows = [False] * n
        diag1 = set()  # i + j
        diag2 = set()  # i - j

        solution_map = {False: '.', True: 'Q'}
        solutions: list[str] = []

        def propagate(row: int, col: int):
            rows[row] = True
            diag1.add(row + col)
            diag2.add(row - col)

        def unpropagate(row: int, col: int):
            rows[row] = False
            diag1.remove(row + col)
            diag2.remove(row - col)

        def can_place(row: int, col: int) -> bool:
            return (not rows[row] and
                    row + col not in diag1 and
                    row - col not in diag2)

        def save_solution():
            solutions.append([
                "".join(solution_map[val] for val in row)
                for row in board
            ])

        def backtrack(col: int):
            if col == n:
                save_solution()
                return
            for row in range(n):
                # try to place queen in [row, col]
                if can_place(row, col):
                    # propagate new constraints
                    propagate(row, col)
                    # backtrack
                    board[row][col] = True
                    backtrack(col + 1)
                    board[row][col] = False
                    # remove constraints
                    unpropagate(row, col)

        backtrack(0)
        return solutions
