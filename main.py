import math
import unittest

class TestIsFinite(unittest.TestCase):
    def is_finite_number(self, x):
        """
        Checks if the given value is finite using math.isfinite().
        :param x: Input value to check
        :return: True if finite, False otherwise
        :raises TypeError: If x is not a number
        :raises ValueError: If x is a special non-numeric value (e.g., NaN)
        """

        if not isinstance(x, (int, float)):
            raise TypeError(f"Input must be a number (int or float), got {type(x).__name__} instead")

        if isinstance(x, float) and math.isnan(x):
            raise ValueError("Input cannot be NaN (Not a Number)")

        self.assertTrue(math.isfinite(x), "X should be finite.")


if __name__=='__main__':
    unittest.main()
