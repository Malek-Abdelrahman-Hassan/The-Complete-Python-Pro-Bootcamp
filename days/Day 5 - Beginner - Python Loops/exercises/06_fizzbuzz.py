"""Coding Exercise 6 - FizzBuzz

Print every number from 1 to 100, including 100.

    divisible by 3 and 5    FizzBuzz
    divisible by 3          Fizz
    divisible by 5          Buzz
    otherwise               the number

The first lines are:

    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz

15 must be FizzBuzz. Test "both" before a test for 3 alone or 5 alone.

Practises: range, modulo, if/elif/else order.
"""

# Write your solution below this line.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)