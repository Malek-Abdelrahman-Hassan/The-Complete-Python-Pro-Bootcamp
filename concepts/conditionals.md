---
tags:
  - concept
aliases:
  - Conditionals
  - if
  - elif
  - else
  - Comparison operators
created: 2026-11-16
---

# Conditionals

## What it is

A conditional runs a block of code only when a condition is true. `if` tests the first condition, `elif` tests another only when earlier tests failed, and `else` runs when none of them were true.

## Why it matters

Programs that only run top to bottom cannot react. Tickets, games, and checks all depend on choosing a branch.

## Syntax

```python
height = 130
if height >= 120:
    print("You can ride.")
elif height >= 100:
    print("With an adult.")
else:
    print("Too short.")
```

The block under each header is indented, normally by four spaces. Comparison operators are `==`, `!=`, `<`, `>`, `<=`, and `>=`. One `=` assigns a value and is not a comparison.

A second `if` after the chain is a new test. It can run even when an earlier branch already ran. An extra `elif` cannot.

## Examples

```python
age = 15
if age < 12:
    bill = 5
elif age <= 18:
    bill = 7
else:
    bill = 12
print(bill)   # 7
```

```python
choice = input("Left or right? ")
if choice.lower() == "left":
    print("You go left.")
else:
    print("You go right.")
```

## Gotchas

> [!WARNING]
> `if x = 1:` is a syntax error. Assignments use `=`. Comparisons use `==`.

- The lines of a block must be indented. Otherwise Python raises `IndentationError: expected an indented block`.
- `"Left" == "left"` is false. Normalise with `.lower()` before comparing typed text.
- Only one branch of an `if`/`elif`/`else` chain runs. A follow-up charge or extra needs its own `if`.
- An `if` does not create a new scope. A name assigned inside the block still exists after the block.

## Related

- [Logical operators](logical-operators.md)
- [Modulo](modulo.md)
- [Errors and debugging](errors-and-debugging.md)

## Appears in

- [Day 3 · Control Flow and Logical Operators](../days/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators.md): `if`/`elif`/`else`, comparisons, and separate `if` statements for the photo add-on
- [Day 6 · Python Functions & Karel](../days/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel.md): `if`/`elif`/`else` choosing the robot's next move in the maze
- [Day 7 · Hangman](../days/Day%207%20-%20Beginner%20-%20Hangman/Day%207%20-%20Beginner%20-%20Hangman.md): letter, earlier correct letter, or blank in `display`
- [Day 9 · Dictionaries, Nesting and the Secret Auction](../days/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction.md): turning scores into grades
