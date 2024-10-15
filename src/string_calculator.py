class StringCalculator:
    def __init__(self):
        pass

    def add(self, number_string):
        if not number_string:
            return 0

        # Replace newline from the number string with comma.
        # numbers = numbers.replace('\n', ',')

        if len(str(number_string)) == 1:
             return int(number_string)

        delimiter = ','
        if number_string.startswith("//"):
            number_string, delimiter = self.get_custom_delimiter(number_string)
        
        numbers = self.split_by_delimiter(number_string, delimiter)
        return self.get_number_sum(numbers)
        
    def get_custom_delimiter(self, number_string):
        delimiter_end_index = number_string.index('\n')
        delimiter = number_string[2:delimiter_end_index]
        number_string = number_string[delimiter_end_index + 1:]
        return number_string, delimiter

    def split_by_delimiter(self, number_string, delimiter):
        return number_string.replace('\n', delimiter).split(delimiter)

    def get_number_sum(self, numbers):
        return sum(int(num) for num in numbers if num.strip())
    

calc = StringCalculator()
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
# print (calc.add("//*\n1*2"))
# print (calc.add("//*\n1*2*3*4*5"))