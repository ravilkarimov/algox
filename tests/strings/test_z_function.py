import unittest
from strings.z_function import z_function, z_function_trivial


class TestZFunction(unittest.TestCase):
    def test_z_function_trivial(self):
        self.assertEqual(z_function_trivial('aaaaa'), [0, 4, 3, 2, 1])
        self.assertEqual(z_function_trivial('aaabaab'), [0, 2, 1, 0, 2, 1, 0])
        self.assertEqual(z_function_trivial('abacaba'), [0, 0, 1, 0, 3, 0, 1])

    def test_z_function(self):
        self.assertEqual(z_function('aaaaa'), [0, 4, 3, 2, 1])
        self.assertEqual(z_function('aaabaab'), [0, 2, 1, 0, 2, 1, 0])
        self.assertEqual(z_function('abacaba'), [0, 0, 1, 0, 3, 0, 1])
        self.assertEqual(z_function('abc$abcab'), [0, 0, 0, 0, 3, 0, 0, 1, 0])

    def test_z_function_edge_cases(self):
        # Test empty string
        self.assertEqual(z_function(''), [])
        # Test single character string
        self.assertEqual(z_function('a'), [0])
        # Test repeating characters
        self.assertEqual(z_function('bbbbbbbb'), [0, 7, 6, 5, 4, 3, 2, 1])
        # Test no repetitions
        self.assertEqual(z_function('abcdef'), [0, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
