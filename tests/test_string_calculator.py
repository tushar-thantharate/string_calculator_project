import unittest
from src.string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        """
        Sets up an instance of StringCalculator.
        """
        self.calc = StringCalculator()

    def test_empty_string(self):
        """
        Test with an empty string. It should return 0
        # Input: “”, Output: 0
        """
        result = self.calc.add("")
        self.assertEqual(result, 0)

    def test_single_number(self):
        """
        Test with a single number as input. It should return same number.
        # Input: “1”, Output: 1
        """

        result = self.calc.add("1")
        self.assertEqual(result, 1)

    def test_multiple_numbers(self):
        """
        Test with two or more comma separated numbers.
        # Input: “1,2,3,4,5”, Output: 15
        """

        result = self.calc.add("1,")
        self.assertEqual(result, 1)

        result = self.calc.add("1,2")
        self.assertEqual(result, 3)

        result = self.calc.add("1,2,3,4,5")
        self.assertEqual(result, 15)

    def test_newline_delimiter(self):
        """
        Test with newline as delimiters.
        # Input: “1\n2,3,4,5”, Output: 15
        """
        result = self.calc.add("1\n2,3")
        self.assertEqual(result, 6)

        result = self.calc.add("1\n2,3\n4,5\n")
        self.assertEqual(result, 15)

    def test_custom_delimiter(self):
        """
        Test with custom delimiters defined by the pattern: //[delimiter]\n[numbers].
        # Input: “//*\n1*2*3*4*5”, Output: 15
        """
        result = self.calc.add("//;\n1;2")
        self.assertEqual(result, 3)

        result = self.calc.add("//*\n1*2")
        self.assertEqual(result, 3)

        result = self.calc.add("//*\n1*2*3*4*5")
        self.assertEqual(result, 15)

        # missing newline
        result = self.calc.add("//*1*2*3*4*5")
        self.assertEqual(result, 0)

    def test_negative_numbers(self):
        """
        Test with a negative number. It should raises a ValueError with an expected message.
        """
        try:
            self.calc.add("1,-2,3")
        except ValueError as e:
            self.assertTrue("Negative numbers not allowed: -2" in str(e))

        # multiple negative numbers
        try:
            self.calc.add("1,-2,-3,4")
        except ValueError as e:
            self.assertTrue("Negative numbers not allowed: -2,-3" in str(e))

    def test_skip_large_numbers(self):
        """
        Test with larger than 1000 number. It should be skipped during cumpuation.
        """
        result = self.calc.add("1001,2")
        self.assertEqual(result, 2)

        result = self.calc.add("1,1001,2,3,4,1002,5")
        self.assertEqual(result, 15)

    def test_mix_cases(self):
        """
        Test with multiple scenarios.
        """
        result = self.calc.add("1\n2,1001,3,4,5")
        self.assertEqual(result, 15)

        result = self.calc.add("//&\n1\n2&1001&3&4&5")
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
