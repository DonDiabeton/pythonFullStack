import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for num in args:
            self.result += num
        return self

    def subtract(self, *args):
        for num in args:
            self.result -= num
        return self

class TestMathDojo(unittest.TestCase):
    def setUp(self):
        self.math_dojo = MathDojo()

    def test_addition(self):
        self.assertEqual(self.math_dojo.add(2, 3, 5).result, 10)
        self.assertEqual(self.math_dojo.add(1, 2).result, 3)

    def test_subtraction(self):
        self.assertEqual(self.math_dojo.subtract(10, 2, 3).result, -15)
        self.assertEqual(self.math_dojo.subtract(5, 1).result, -6)

    def test_mixed_operations(self):
        self.assertEqual(self.math_dojo.add(5, 10).subtract(3).add(8).result, 20)

if __name__ == '__main__':
    unittest.main()
