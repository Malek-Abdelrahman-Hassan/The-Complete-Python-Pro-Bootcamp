"""Day 10 Project - Calculator

A text calculator that can keep working with its last answer.
Target: https://appbrewery.github.io/python-day10-demo/

Requirements:

1. Write add, subtract, multiply, and divide. Each takes n1 and n2 and
   returns the result.
2. Store the four functions in a dictionary, operations, under the keys
   "+", "-", "*", "/". Store the function itself, without parentheses.
3. Ask "What's the first number?: " and convert it with float().
4. Print the four symbols, then ask "Pick an operation: ".
5. Ask "What's the next number?: ". Look up the function with
   operations[symbol], call it, and print the whole calculation:
       5.0 * 3.0 = 15.0
6. Ask "Type 'y' to continue calculating with 15.0, or type 'n' to start
   a new calculation: ". On "y", the answer becomes the first number.
   On "n", print some blank lines and start again from step 3.
7. Print art.logo when the calculator starts.

Run from this day's folder:
    python project/main.py
"""

# Write your solution below this line.

import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start "
            "a new calculation: "
        ) == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 25)
            calculator()


calculator()