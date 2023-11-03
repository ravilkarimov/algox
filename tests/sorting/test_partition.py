import unittest
from sorting.partition import partition


class TestPartitionFunction(unittest.TestCase):
    def test_empty_array(self):
        arr, k = [], 0
        partition_indices = partition(arr, 0, len(arr) - 1, k)
        self.assertEqual(partition_indices, (-1, -1))
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr, k = [1], 0
        partition_indices = partition(arr, 0, len(arr) - 1, k)
        self.assertEqual(partition_indices, (0, 0))
        self.assertEqual(arr, [1])

    def test_two_elements(self):
        arr, k = [2, 1], 1
        partition_indices = partition(arr, 0, len(arr) - 1, k)
        self.assertTrue(all(arr[i] <= arr[partition_indices[1]] for i in range(partition_indices[0])))
        self.assertTrue(all(arr[i] >= arr[partition_indices[0]] for i in range(partition_indices[1]+1, len(arr))))
        self.assertEqual(sorted(arr), arr)

    def test_multiple_elements(self):
        arr, k = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 5
        partition_indices = partition(arr, 0, len(arr) - 1, k)
        left_of_pivot = arr[:partition_indices[0]]
        right_of_pivot = arr[partition_indices[1]+1:]

        self.assertTrue(all(x < arr[partition_indices[0]] for x in left_of_pivot))
        self.assertTrue(all(x > arr[partition_indices[1]] for x in right_of_pivot))

    def test_all_equal_elements(self):
        arr, k = [1, 1, 1, 1], 2
        partition_indices = partition(arr, 0, len(arr) - 1, k)
        self.assertEqual(partition_indices, (0, len(arr) - 1))
        self.assertEqual(arr, [1, 1, 1, 1])

    def test_already_sorted(self):
        arr, k = [1, 2, 3, 4, 5], 2
        partition_indices = partition(arr, 0, len(arr) - 1, k)
        self.assertTrue(all(arr[i] <= arr[partition_indices[1]] for i in range(partition_indices[0])))
        self.assertTrue(all(arr[i] >= arr[partition_indices[0]] for i in range(partition_indices[1]+1, len(arr))))
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr, k = [5, 4, 3, 2, 1], 2
        partition_indices = partition(arr, 0, len(arr) - 1, k)
        left_of_pivot = arr[:partition_indices[0]]
        right_of_pivot = arr[partition_indices[1]+1:]

        self.assertTrue(all(x <= arr[partition_indices[0]] for x in left_of_pivot))
        self.assertTrue(all(x >= arr[partition_indices[1]] for x in right_of_pivot))

    def test_duplicate_elements(self):
        arr, k = [3, 6, 3, 8, 4, 3, 1, 2], 3
        partition_indices = partition(arr, 0, len(arr) - 1, k)
        left_of_pivot = arr[:partition_indices[0]]
        right_of_pivot = arr[partition_indices[1]+1:]

        self.assertTrue(all(x < arr[partition_indices[0]] for x in left_of_pivot))
        self.assertTrue(all(x > arr[partition_indices[1]] for x in right_of_pivot))

if __name__ == "__main__":
    unittest.main()
