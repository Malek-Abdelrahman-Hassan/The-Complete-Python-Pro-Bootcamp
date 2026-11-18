---
tags:
  - index
---

# Glossary

One-line definitions of the terms used across the notes, in alphabetical order. Topics that need more than a line have their own page in [Concepts](concepts.md).

| Term | Definition | First seen |
| --- | --- | --- |
| `append()` | A list method that adds one item at the end of the list. | Day 4 |
| Assignment | Storing a value under a variable name with `=`. | Day 1 |
| Assignment operator | A shorthand such as `+=` or `-=` that updates a variable using its previous value. | Day 2 |
| Boolean (`bool`) | A data type with only two values: `True` or `False`. | Day 2 |
| Bug | A mistake in code that makes it fail or behave unexpectedly. | Day 1 |
| Case-sensitive | Treating capital and lowercase letters as different, so `city` and `City` are two names. | Day 1 |
| Code block | The indented lines that belong to one statement, such as `if`, `elif`, `else`, or `for`. | Day 3 |
| Comment | Text after `#` that Python ignores; used for notes in code. | Day 1 |
| Comparison operator | An operator that compares two values and gives `True` or `False`, such as `==`, `!=`, `<`, `>`, `<=`, or `>=`. | Day 3 |
| Concatenation | Joining strings end to end with `+`. | Day 1 |
| Conditional | A statement that runs code only when a condition is true. | Day 3 |
| Console | The area where a program prints its output and reads typed input. | Day 1 |
| Debugging | Finding and fixing the causes of errors in code. | Day 1 |
| `elif` | A branch that is tested only when every `if` and `elif` above it was false. | Day 3 |
| `else` | The branch that runs when every condition above it was false. | Day 3 |
| Exit code | The number a program reports when it ends; `0` means it finished without errors. | Day 1 |
| Exponent (`**`) | The operator that raises a number to a power, such as `2 ** 3` for 8. | Day 2 |
| `extend()` | A list method that adds each item from another list onto the end. | Day 4 |
| Float | A data type for numbers with a decimal point, such as `3.14` or `2.0`. | Day 2 |
| Floor division (`//`) | Division that drops the fractional part and keeps an integer, such as `5 // 3` → `1`. | Day 2 |
| `for` loop | A loop that runs its indented block once for each item in a list, or once for each value from `range`. | Day 5 |
| f-string | A string with an `f` before the quotes; `{name}` placeholders are filled in automatically. | Day 2 |
| Function | A named piece of code that does a job when called with parentheses, such as `print()`. | Day 1 |
| IDE | Integrated development environment: a code editor with tools for running and debugging, such as PyCharm. | Day 1 |
| `if` statement | A conditional that runs its indented block only when its condition is true. | Day 3 |
| `IndentationError` | The error raised when spaces or tabs at the start of a line are unexpected or missing. | Day 1 |
| Index | The position of an item in a string or a list. The first item is index `0`. Index `-1` is the last item. | Day 2 |
| `IndexError` | The error raised when an index does not exist, such as `items[len(items)]`. The message is `list index out of range`. | Day 4 |
| Integer (`int`) | A data type for whole numbers without decimal places, such as `42` or `-3`. | Day 2 |
| Keyword | A word reserved by Python, such as `if` or `class`, that cannot be used as a name. | Day 1 |
| List | An ordered collection of items in square brackets, such as `["a", "b"]`. | Day 4 |
| Logical operator | `and`, `or`, or `not`: words that combine two conditions or invert one. | Day 3 |
| Module | A Python file of related code. `import random` loads the `random` module so its functions can be called as `random.randint`. | Day 4 |
| Modulo (`%`) | The operator that gives the remainder of a division, such as `7 % 2` → `1`. | Day 3 |
| `NameError` | The error raised when code uses a name that has not been defined. | Day 1 |
| Nested `if` | An `if` statement placed inside the block of another `if` or `else`. | Day 3 |
| Nested list | A list stored as an item inside another list. `pairs[0][1]` reads the second item of the first inner list. | Day 4 |
| New line (`\n`) | A special character sequence inside a string that starts a new line. | Day 1 |
| PEMDAS | The order of operations: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction (left to right within each level). | Day 2 |
| PEP 8 | The official style guide for Python code. | Day 1 |
| Primitive data type | One of the four built-in types met first: `str`, `int`, `float`, `bool`. | Day 2 |
| Prompt | The message `input()` shows before waiting for the user to type. | Day 1 |
| `random.choice()` | A function that returns one item from a sequence, chosen at random. | Day 4 |
| `random.randint()` | A function that returns a random integer from `a` to `b`, including both ends. | Day 4 |
| `random.random()` | A function that returns a random float from 0 inclusive up to, but not including, 1. | Day 4 |
| `random.shuffle()` | A function that reorders a list in place and returns `None`. | Day 5 |
| `range()` | A function that produces integers from a start up to, but not including, a stop. A third argument is the step. | Day 5 |
| Round (`round()`) | A function that rounds a number; `round(3.6)` is `4`, and `round(3.14159, 2)` keeps two decimal places. | Day 2 |
| Snake case | A naming style of lowercase words joined by underscores, such as `pet_name`. | Day 1 |
| String | A sequence of characters between quotes; Python's type for text. | Day 1 |
| Subscripting | Pulling one character from a string with square brackets, such as `"hello"[0]`. | Day 2 |
| Syntax | The grammar rules that code has to follow. | Day 1 |
| Syntax highlighting | Colouring code by its role, so that strings, names and mistakes stand out. | Day 1 |
| `SyntaxError` | The error raised when code breaks Python's grammar rules. | Day 1 |
| Traceback | The report Python prints when an error stops a program, ending with the error type and message. | Day 1 |
| Type checking | Using `type(value)` to see which data type a value has. | Day 2 |
| Type conversion | Turning a value into another type with `int()`, `float()`, `str()` or `bool()`. | Day 2 |
| `TypeError` | The error raised when an operation does not work on the types given, such as `len(123)`. | Day 2 |
| `ValueError` | The error raised when a conversion fails, such as `int("abc")`. | Day 2 |
| Variable | A name that refers to a stored value. | Day 1 |
