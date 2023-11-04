import unittest
from sorting.radixsort import radix_sort


class TestRadixSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(radix_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(radix_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(radix_sort([1, 2, 3]), [1, 2, 3])

    def test_reverse_sorted_list(self):
        self.assertEqual(radix_sort([3, 2, 1]), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(radix_sort([-2, -1, -3]), [-3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(radix_sort([-2, 3, 1, -1, 0]), [-2, -1, 0, 1, 3])

    def test_large_numbers(self):
        self.assertEqual(radix_sort([123, 456, 789]), [123, 456, 789])

    def test_zeros_and_negatives(self):
        self.assertEqual(radix_sort([0, -1, -2, 0]), [-2, -1, 0, 0])

    def test_same_numbers(self):
        self.assertEqual(radix_sort([5, 5, 5]), [5, 5, 5])

    def test_large_range(self):
        self.assertEqual(radix_sort(list(range(-1000, 1000))), list(range(-1000, 1000)))

if __name__ == '__main__':
    unittest.main()
