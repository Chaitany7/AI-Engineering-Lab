import unittest

from src.main import add, power, subtract


class TestArithmeticFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_and_positive_numbers(self):
        self.assertEqual(add(-4, 7), 3)

    def test_add_zero(self):
        self.assertEqual(add(0, 9), 9)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -3)

    def test_subtract_zero(self):
        self.assertEqual(subtract(8, 0), 8)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)


if __name__ == "__main__":
    unittest.main()
