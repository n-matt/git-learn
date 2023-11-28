import unittest

from src.calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator()

    def test_add(self):
        assert self.cal.add(1, 2) == 3.0
        assert self.cal.add(1.0, 2.0) == 3.0
        assert self.cal.add(0, 2.0) == 2.0
        assert self.cal.add(2.0, 0) == 2.0
        assert self.cal.add(-4, 2.0) == -2.0

    def test_subtract(self):
        assert self.cal.subtract(1, 2) == -1.0
        assert self.cal.subtract(2, 1) == 1.0
        assert self.cal.subtract(1.0, 2.0) == -1.0
        assert self.cal.subtract(0, 2.0) == -2.0
        assert self.cal.subtract(2.0, 0.0) == 2.0
        assert self.cal.subtract(-4, 2.0) == -6.0

    def test_multiply(self):
        assert self.cal.multiply(1, 2) == 2.0
        assert self.cal.multiply(1.0, 2.0) == 2.0
        assert self.cal.multiply(0, 2.0) == 0.0
        assert self.cal.multiply(2.0, 0.0) == 0.0
        assert self.cal.multiply(-4, 2.0) == -8.0

    def test_divide(self):
        assert self.cal.divide(1, 2) == 0.5
        assert self.cal.divide(1.0, 2.0) == 0.5
        assert self.cal.divide(0, 2.0) == 0
        assert self.cal.divide(-4, 2.0) == -2.0
        assert self.cal.divide(10, 0) == 'Cannot divide by 0'
