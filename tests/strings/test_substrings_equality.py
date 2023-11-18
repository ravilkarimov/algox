import unittest
from strings.substrings_const_equality import SubStringEquality


class TestSubStringEqualityFunction(unittest.TestCase):
    def test_simple_case(self):
        solution = SubStringEquality("acabaca")
        self.assertEqual(solution.is_equal(4, 3, 2), False)
        self.assertEqual(solution.is_equal(3, 4, 0), True)
        self.assertEqual(solution.is_equal(2, 0, 1), False)


if __name__ == '__main__':
    unittest.main()
