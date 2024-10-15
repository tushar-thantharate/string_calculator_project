class StringCalculator:
    def __init__(self):
        pass

    def add(self, number_string):
        """
        Takes a string of numbers, which can include custom delimiters and
        newline characters, and returns their sum.
        """
        # If the input is empty, return 0
        if not number_string:
            return 0

        # If there is only one character, return same number
        if len(str(number_string)) == 1:
            return int(number_string)

        delimiter = ","
        # Check if the number string starts with a custom delimiter pattern
        if number_string.startswith("//"):
            status, number_string, delimiter = self.get_custom_delimiter(number_string)
            # exit if no newline found.
            if not status:
                return 0

        # Split the numbers using the idenfied delimiter
        numbers = self.split_by_delimiter(number_string, delimiter)

        # Check if any negative numbers present and raise an error if found
        self.check_for_negative_numbers(numbers)

        # Compute and return the sum of the numbers
        return self.get_number_sum(numbers)

    def get_custom_delimiter(self, number_string):
        """
        Extracts a custom delimiter from the input string based on the pattern
         Pattern: "//[delimiter]\n[numbers…]"
        """
        newline_exists = number_string.find("\n")
        if newline_exists == -1:
            return (
                False,
                "Number string must contain a newline for custom delimiter.",
                "",
            )

        delimiter_end_index = number_string.index("\n")
        delimiter = number_string[2:delimiter_end_index].strip()
        number_string = number_string[delimiter_end_index + 1 :]
        return True, number_string, delimiter

    def split_by_delimiter(self, number_string, delimiter):
        """
        Splits the number string using the provided delimiter.
        """
        return number_string.replace("\n", delimiter).split(delimiter)

    def get_number_sum(self, numbers):
        """
        Compute the sum of the provided number strings, skip any
        numbers greater than 1000.
        """
        return sum(
            int(num)
            for num in numbers
            if num.strip() and int(num) <= 1000
            if num.strip().isdigit()
        )

    def check_for_negative_numbers(self, numbers):
        """
        Checks if any number is negative and raise ValueError.
        """
        negative_numbers = [num for num in numbers if num and int(num) < 0]
        if negative_numbers:
            raise ValueError(
                "Negative numbers not allowed: {}".format(
                    ",".join([str(num) for num in negative_numbers])
                )
            )


# calc = StringCalculator()
# print (calc.add(""))
# print (calc.add(None))

# print (calc.add('1'))

# print (calc.add('1,'))
# print (calc.add('1,2'))
# print (calc.add('1,2,3,4,5'))

# print (calc.add('1\n'))
# print (calc.add('1\n2,3'))
# print (calc.add('1\n2,3\n4,5\n'))

# print (calc.add("//;\n1;2"))
# # print (calc.add("//*\n1*2"))
# # print (calc.add("//*\n1*2*3*4*5"))
# print (calc.add("//*1*2*3*4*5"))

# print (calc.add("1,-2,3"))
# print (calc.add("1,-2,-3,4"))

# print (calc.add("1001,2"))
# print (calc.add("1,1001,2,3,4,1002,5"))
