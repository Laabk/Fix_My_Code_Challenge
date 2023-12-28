#!/usr/bin/python3
""" FizzBuzz: printing numbers base on the outcome of divisible of 3 and 5
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n with spaces
    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    _result = []
    for ite in range(1, n + 1):
        if (ite % 3) == 0 and (ite % 5) == 0:
            _result.append("FizzBuzz")
        elif (ite % 3) == 0:
            _result.append("Fizz")
        elif (ite % 5) == 0:
            _result.append("Buzz")
        else:
            _result.append(str(i))
    print(" ".join(_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
