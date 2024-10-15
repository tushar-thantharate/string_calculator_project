# String Calculator

A Python implementation of a simple string calculator that takes a string of numbers, separated by custom or default delimiters, and returns their sum. The project demonstrates a TDD approach with comprehensive test cases to ensure correct functionality.

## Features

- Handles an empty string as input, returning `0`.
- Adds numbers separated by commas (e.g., `"1,2,3"`).
- Supports newlines as delimiters (e.g., `"1\n2,3"`).
- Supports custom delimiters (e.g., `"//[delimiter]\n[numbers…]"`).
- Ignores numbers greater than `1000`.
- Raises an exception for negative numbers and lists all negative values in the error message.

## Requirements

- Python 3.x
- `pytest`

## Usage

To use the string calculator, simply create an instance of the `StringCalculator` class and call the `add` method with a string of numbers.

Example:

```python
from src.string_calculator import StringCalculator

calc = StringCalculator()
result = calc.add("1,2,3")
print(result)  # Output: 6

result = calc.add("1\n2")
print(result)  # Output: 3
