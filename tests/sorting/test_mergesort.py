import random
import unittest
from sorting.mergesort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_all_identical_elements(self):
        self.assertEqual(merge_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_single_element_array(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_large_array(self):
        large_array = [random.randint(-1000, 1000) for _ in range(10000)]
        self.assertEqual(merge_sort(large_array), sorted(large_array))

    def test_random_unsorted_array(self):
        random_array = [random.randint(1, 100) for _ in range(10)]
        self.assertEqual(merge_sort(random_array), sorted(random_array))

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-5, -1, -3, -2, -4]), [-5, -4, -3, -2, -1])

    def test_negative_and_positive_numbers(self):
        self.assertEqual(merge_sort([-1, 2, -3, 4, -5, 6]), [-5, -3, -1, 2, 4, 6])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            merge_sort([1, 'two', 3])


if __name__ == '__main__':
    unittest.main()
