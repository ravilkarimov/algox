import unittest
from sorting.countingsort import counting_sort


class TestCountingSort(unittest.TestCase):

    def test_sort_positive_numbers(self):
        self.assertEqual(counting_sort([4, 2, 3, 1, 5]), [1, 2, 3, 4, 5])

    def test_sort_negative_numbers(self):
        self.assertEqual(counting_sort([-4, -2, -3, -1, -5]), [-5, -4, -3, -2, -1])

    def test_sort_mixed_numbers(self):
        self.assertEqual(counting_sort([3, -2, -1, 4, 0]), [-2, -1, 0, 3, 4])

    def test_sort_already_sorted(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        self.assertEqual(counting_sort([1]), [1])

    def test_sort_empty_array(self):
        self.assertEqual(counting_sort([]), [])

    def test_sort_duplicates(self):
        self.assertEqual(counting_sort([2, 3, 3, 2, 1]), [1, 2, 2, 3, 3])

    def test_sort_large_range(self):
        self.assertEqual(counting_sort([-100000, 100000]), [-100000, 100000])

    def test_sort_with_zero(self):
        self.assertEqual(counting_sort([0, -1, 1]), [-1, 0, 1])


if __name__ == '__main__':
    unittest.main()
