import os
import time
import unittest
import numpy as np
from ml.supervised.knn import KNearestNeighbor
from sklearn.neighbors import KNeighborsClassifier


class TestKNearestNeighbor(unittest.TestCase):

    def setUp(self):
        self.X_train = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
        self.y_train = np.array([0, 1, 0, 1])
        self.X_test = np.array([[1, 1], [2, 2]])
        self.knn = KNearestNeighbor()
        self.knn.fit(self.X_train, self.y_train)
        self.sk_knn = KNeighborsClassifier(n_neighbors=1)
        self.sk_knn.fit(self.X_train, self.y_train)

    def test_predict_labels(self):
        dists = self.knn.compute_distances_no_loops(self.X_test)
        y_test_pred = self.knn.predict_labels(dists, k=1)
        sk_y_test_pred = self.sk_knn.predict(self.X_test)
        self.assertTrue(np.array_equal(y_test_pred, sk_y_test_pred))

    def test_sklearn_compatibility(self):
        # Directly compare the predictions of the two implementations
        sk_knn = KNeighborsClassifier(n_neighbors=1)
        sk_knn.fit(self.X_train, self.y_train)
        sk_y_pred = sk_knn.predict(self.X_test)

        y_pred = self.knn.predict(self.X_test, k=1)
        np.testing.assert_array_equal(y_pred, sk_y_pred)

    def test_compute_distances_no_loops(self):
        dists = self.knn.compute_distances_no_loops(self.X_test)
        correct_dists = np.array([[1., 1., 3.60555128, 3.60555128],
                                  [1., 1., 2.23606798, 2.23606798]])
        np.testing.assert_almost_equal(dists, correct_dists, decimal=7)

    def test_compute_distances_one_loop(self):
        dists = self.knn.compute_distances_one_loop(self.X_test)
        correct_dists = np.array([[1., 1., 3.60555128, 3.60555128],
                                  [1., 1., 2.23606798, 2.23606798]])
        np.testing.assert_almost_equal(dists, correct_dists, decimal=7)

    def test_compute_distances_two_loops(self):
        dists = self.knn.compute_distances_two_loops(self.X_test)
        correct_dists = np.array([[1., 1., 3.60555128, 3.60555128],
                                  [1., 1., 2.23606798, 2.23606798]])
        np.testing.assert_almost_equal(dists, correct_dists, decimal=7)


@unittest.skipIf(os.environ.get('RUN_PERF_TESTS') != '1', "Performance tests are disabled")
class TestKNearestNeighborPerformance(unittest.TestCase):
    def setUp(self):
        # Setting up a dataset for performance testing.
        self.num_train = 1000
        self.num_test = 1000
        self.dimension = 50
        self.X_train = np.random.randn(self.num_train, self.dimension)
        self.X_test = np.random.randn(self.num_test, self.dimension)
        self.y_train = np.random.randint(0, 10, self.num_train)
        self.knn = KNearestNeighbor()
        self.knn.fit(self.X_train, self.y_train)

    def test_performance(self):
        # Measure performance of compute_distances_two_loops
        start_time = time.time()
        dists_two_loops = self.knn.compute_distances_two_loops(self.X_test)
        time_two_loops = time.time() - start_time

        # Measure performance of compute_distances_one_loop
        start_time = time.time()
        dists_one_loop = self.knn.compute_distances_one_loop(self.X_test)
        time_one_loop = time.time() - start_time

        # Measure performance of compute_distances_no_loops
        start_time = time.time()
        dists_no_loops = self.knn.compute_distances_no_loops(self.X_test)
        time_no_loops = time.time() - start_time

        # You can print out the times or make assertions about them.
        print(f"Two loops: {time_two_loops}s")
        print(f"One loop: {time_one_loop}s")
        print(f"No loops: {time_no_loops}s")

        # If you want to enforce performance constraints
        self.assertLess(time_one_loop, time_two_loops)
        self.assertLess(time_no_loops, time_one_loop)

        # Ensure that all methods return the correct results
        np.testing.assert_array_almost_equal(dists_two_loops, dists_one_loop)
        np.testing.assert_array_almost_equal(dists_one_loop, dists_no_loops)


if __name__ == '__main__':
    unittest.main()
