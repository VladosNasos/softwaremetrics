import math
import unittest

class TestIsFinite(unittest.TestCase):
    def test_isfinite_with_integers(self):
        # These should all be finite
        self.assertTrue(math.isfinite(0), "0 should be finite.")
        self.assertTrue(math.isfinite(42), "42 should be finite.")
        self.assertTrue(math.isfinite(-100), "-100 should be finite.")
    
    def test_isfinite_with_floats(self):
        # Floats (including negatives) that aren't infinite or NaN are finite
        self.assertTrue(math.isfinite(3.14), "3.14 should be finite.")
        self.assertTrue(math.isfinite(-2.71828), "-2.71828 should be finite.")
    
    def test_isfinite_with_infinity(self):
        # Positive and negative infinity should not be finite
        self.assertFalse(math.isfinite(float('inf')), "inf should NOT be finite.")
        self.assertFalse(math.isfinite(float('-inf')), "-inf should NOT be finite.")
    
    def test_isfinite_with_nan(self):
        # Not a Number should not be finite
        self.assertFalse(math.isfinite(float('nan')), "NaN should NOT be finite.")

# TDD note:
# 1. You'd write these tests first (they fail if you haven’t implemented the function or usage).
# 2. Then write or fix the code that calls math.isfinite so all tests pass.
