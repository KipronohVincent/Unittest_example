import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        # result = calculator.add(10, 5)
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(100, 5), 105)

    
    def test_sub(self):
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(-1, 1), -2)
        self.assertEqual(calculator.sub(100, 5), 95)
        

    def test_mul(self):
        self.assertEqual(calculator.mul(10, 5), 50)
        self.assertEqual(calculator.mul(-1, 1), -1)
        self.assertEqual(calculator.mul(100, 5), 500)

    def test_div(self):
        self.assertEqual(calculator.div(15, 5), 3)
        self.assertEqual(calculator.div(-1, 1), -1)
        self.assertEqual(calculator.div(100, 5), 20)

        # self.assertRaises(ValueError, calculator.div, 5, 0)
        with self.assertRaises(ValueError):
            calculator.div(3, 0)

if __name__ == '__main__':
    unittest.main()