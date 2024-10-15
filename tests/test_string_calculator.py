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


if __name__ == '__main__':
    unittest.main()