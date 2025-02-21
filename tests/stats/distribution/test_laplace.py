import unittest
import numpy as np
from scipy.stats import laplace as sp_laplace
from stats.distribution.laplace import LaplaceDistribution


class TestLaplaceDistribution(unittest.TestCase):

    def test_mean_abs_deviation_from_median(self):
        # Test data
        x = np.array([[1, 2], [3, 4], [5, 6]])
        expected_mad = np.array([4/3, 4/3])

        # Calculate mean absolute deviation from median
        mad = LaplaceDistribution.mean_abs_deviation_from_median(x)

        # Assert equality
        np.testing.assert_array_equal(mad, expected_mad)

    def test_init(self):
        # Test data
        features = np.array([[1, 2], [3, 4], [5, 6]])

        # Expected results
        expected_loc = np.array([3, 4])
        expected_scale = np.array([4/3, 4/3])

        # Initialize distribution
        dist = LaplaceDistribution(features)

        # Assert equality
        np.testing.assert_array_equal(dist.loc, expected_loc)
        np.testing.assert_array_equal(dist.scale, expected_scale)

    def test_logpdf(self):
        # Initialize distribution
        features = np.array([[1, 2], [3, 4], [5, 6]])
        dist = LaplaceDistribution(features)

        # Test data
        values = np.array([[2, 2], [3, 4]])

        # Expected results
        expected_logpdf = np.log(0.5 * np.exp(-np.abs(values - dist.loc) / dist.scale) / dist.scale)

        # Calculate logpdf
        logpdf = dist.logpdf(values)

        # Assert equality
        np.testing.assert_array_almost_equal(logpdf, expected_logpdf)

    def test_pdf(self):
        # Initialize distribution
        features = np.array([[1, 2], [3, 4], [5, 6]])
        dist = LaplaceDistribution(features)

        # Test data
        values = np.array([[2, 2], [3, 4]])

        # Expected results
        expected_pdf = np.exp(dist.logpdf(values))

        # Calculate pdf
        pdf = dist.pdf(values)

        # Assert equality
        np.testing.assert_array_almost_equal(pdf, expected_pdf)

    def test_compare_with_scipy_logpdf(self):
        features = np.array([[1, 2], [3, 4], [5, 6]])
        dist = LaplaceDistribution(features)
        values = np.array([[2, 2], [3, 4]])

        # Calculate logpdf using the custom class
        class_logpdf = dist.logpdf(values)

        # Calculate logpdf using scipy
        scipy_logpdf = sp_laplace.logpdf(values, loc=dist.loc, scale=dist.scale)

        # Assert equality
        np.testing.assert_array_almost_equal(class_logpdf, scipy_logpdf)

    def test_compare_with_scipy_pdf(self):
        features = np.array([[1, 2], [3, 4], [5, 6]])
        dist = LaplaceDistribution(features)
        values = np.array([[2, 2], [3, 4]])

        # Calculate pdf using the custom class
        class_pdf = dist.pdf(values)

        # Calculate pdf using scipy
        scipy_pdf = sp_laplace.pdf(values, loc=dist.loc, scale=dist.scale)

        # Assert equality
        np.testing.assert_array_almost_equal(class_pdf, scipy_pdf)


if __name__ == '__main__':
    unittest.main()
