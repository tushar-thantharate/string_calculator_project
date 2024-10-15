class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers):
        if not numbers:
            return 0

        if len(str(numbers)) == 1:
             return int(numbers)

calc = StringCalculator()
# print (calc.add(""))
# print (calc.add(None))
print (calc.add('1'))