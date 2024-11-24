import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)  # Starter code
        self.assertEqual(self.calc.add(-1, -1), -2)  # Negative numbers

    # Test cases for subtract()
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Regular subtraction
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Negative result

    # Test cases for multiply()
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)  # Regular multiplication
        self.assertEqual(self.calc.multiply(0, 10), 0)  # Multiplying by zero

    # Test cases for divide()
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  # Regular division
        with self.assertRaises(ZeroDivisionError):  # Divide by zero
            self.calc.divide(10, 0)

    # Test cases for modulo()
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  # Regular modulo
        self.assertEqual(self.calc.modulo(5, 1), 0)  # Modulo by 1
    
if __name__ == '__main__':
    unittest.main()
