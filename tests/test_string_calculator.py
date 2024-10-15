import unittest
from src.string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        # Input: “”, Output: 0
        result = self.calc.add("")
        self.assertEqual(result, 0)

    def test_single_number(self):
        # Input: “1”, Output: 1
        result = self.calc.add("1")
        self.assertEqual(result, 1)

    def test_multiple_numbers(self):
        result = self.calc.add("1,")
        self.assertEqual(result, 1)

        result = self.calc.add("1,2")
        self.assertEqual(result, 3)

        result = self.calc.add("1,2,3,4,5")
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()