import unittest
from sorting.quicksort import quicksort


class TestQuicksortFunction(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        self.assertEqual(quicksort(arr, 0, len(arr) - 1), [])

    def test_single_element(self):
        arr = [1]
        self.assertEqual(quicksort(arr, 0, len(arr) - 1), [1])

    def test_two_elements(self):
        arr = [2, 1]
        self.assertEqual(quicksort(arr, 0, len(arr) - 1), [1, 2])

    def test_sorted_desc_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(quicksort(arr, 0, len(arr) - 1), [1, 2, 3, 4, 5])
