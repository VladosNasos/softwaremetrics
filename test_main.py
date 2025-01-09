import unittest
from main import is_finite_number

class TestIsFiniteNumber(unittest.TestCase):
    def test_finite_numbers(self):
        self.assertTrue(is_finite_number(5))  # Integer
        self.assertTrue(is_finite_number(3.14))  # Float
        self.assertTrue(is_finite_number(-100))  # Negative number

    def test_infinite_numbers(self):
        self.assertFalse(is_finite_number(float('inf')))  # Positive infinity
        self.assertFalse(is_finite_number(float('-inf')))  # Negative infinity

    def test_nan(self):
        self.assertFalse(is_finite_number(float('nan')))  # Not a Number (NaN)

if __name__ == '__main__':
    unittest.main()
