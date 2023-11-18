import unittest

from other.backtrack import NQueens


class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = NQueens()

    def test_4_queens(self):
        result = self.solution.solve(4)
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."]
        ]
        self.assertEqual(len(result), len(expected))
        for solution in expected:
            self.assertIn(solution, result)

    def test_1_queen(self):
        result = self.solution.solve(1)
        expected = [["Q"]]
        self.assertEqual(result, expected)

    def test_0_queen(self):
        result = self.solution.solve(0)
        expected = []
        self.assertEqual(result, expected)

    def test_3_queens(self):
        result = self.solution.solve(3)
        expected = []  # No solution for 3 queens
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
