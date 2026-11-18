---
tags:
  - concept
aliases:
  - print()
  - input()
created: 2026-09-26
---

# Input and output

## What it is

Output is anything a program shows to the user; input is data the user gives to the program. In a console program, `print()` produces output and `input()` collects input.

## Why it matters

Input and output turn a script that always does the same thing into an interactive program that responds to whoever runs it.

## Syntax

```python
print(value)    # shows the value, then moves to a new line
input(prompt)   # shows the prompt, waits for Enter, returns the typed text as a string
```

## Examples

```python
print("Welcome!")

name = input("What is your name? ")
print("Hello " + name)

# Cursor waits on the line below the prompt
city = input("Which city did you grow up in?\n")

# Nested call: input() is evaluated first, then print() shows the result
print("Hi " + input("Name? ") + "!")
```

```text
Welcome!
What is your name? Ada
Hello Ada
Which city did you grow up in?
Cairo
Name? Ada
Hi Ada!
```

## Gotchas

> [!WARNING]
> `input()` always returns a string, even when the user types a number. Use `int()` or `float()` before doing maths. See [Type conversion](type-conversion.md).

- The prompt is printed exactly as written. End it with a space (`"Name? "`) or `\n` so the answer does not stick to the prompt.
- While `input()` waits, the program is paused, not frozen: click into the console, type and press Enter.
- Python evaluates nested calls from the inside out, so an `input()` inside a `print()` runs first.

## Related

- [Strings](strings.md)
- [Variables](variables.md)

## Appears in

- [Day 1 · Working with Variables in Python to Manage Data](../days/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data.md): `print()`, `input()` and nesting `input()` inside `print()`
- [Day 2 · Understanding Data Types and How to Manipulate Strings](../days/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings.md): reading numeric answers with `float()` and `int()`
- [Day 3 · Control Flow and Logical Operators](../days/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators.md): reading a choice and printing the branch that matched
- [Day 4 · Randomisation and Python Lists](../days/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists.md): `int(input(...))` for a Rock Paper Scissors choice
- [Day 5 · Python Loops](../days/Day%205%20-%20Beginner%20-%20Python%20Loops/Day%205%20-%20Beginner%20-%20Python%20Loops.md): three `int(input(...))` questions for the password generator
