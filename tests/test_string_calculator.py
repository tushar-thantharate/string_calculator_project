import unittest
from src.string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        # Input: “”, Output: 0
        calc = StringCalculator()
        result = calc.add("")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()