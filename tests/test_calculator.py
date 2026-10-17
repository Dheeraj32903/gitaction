import unittest
from src.calculator import add, subtract, multiply, divide, power, is_even


class TestCalculator(unittest.TestCase):
    """Unit tests for the calculator module."""

    def test_add(self):
        """Test addition of positive and negative numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 7), -7)
        self.assertEqual(subtract(-3, -3), 0)

    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        """Test standard division."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 3), -2)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        """Test power calculation."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(9, 0.5), 3.0)

    def test_is_even(self):
        """Test is_even function."""
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-1))
        with self.assertRaises(TypeError):
            is_even("hello")


if __name__ == '__main__':
    unittest.main()
