class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers):
        if not numbers:
            return 0

        # Replace newline from the number string with comma.
        numbers = numbers.replace('\n', ',')

        if len(str(numbers)) == 1:
             return int(numbers)

        return sum(int(num) for num in numbers.split(',') if num.strip())


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