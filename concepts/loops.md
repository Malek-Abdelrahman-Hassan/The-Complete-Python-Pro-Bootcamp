---
tags:
  - concept
aliases:
  - Loops
  - for loop
  - range
created: 2026-11-18
---

# Loops

## What it is

A `for` loop runs a block once for every item in a collection, or once for every integer `range` produces. The name after `for` refers to the current item and changes on each pass.

## Why it matters

Adding fifty scores by hand is a new line per score. A loop is one block that works for a list of any length.

## Syntax

```python
for fruit in ["apple", "peach", "pear"]:
    print(fruit)               # once per item

for number in range(1, 11):
    print(number)              # 1 through 10; 11 is not included

for number in range(1, 11, 3):
    print(number)              # 1, 4, 7, 10
```

Lines indented under `for` repeat. A line at the same indent as `for`, written below the loop, runs once after the last pass.

## Examples

```python
total = 0
for number in range(1, 101):
    total += number
print(total)                   # 5050, the sum of 1 through 100

scores = [8, 15, 3]
max_score = 0
for score in scores:
    if score > max_score:
        max_score = score
```

`range` by itself prints nothing useful. The loop is what pulls each number out.

## Gotchas

> [!WARNING]
> `range(1, 100)` stops at 99. To include 100, the stop is 101.

- Printing an accumulator inside the loop shows every partial result. Print it after the loop when only the final value matters.
- A `for` body that is not indented raises `IndentationError`.

## Related

- [Lists](lists.md)
- [Random](random.md)
- [Modulo](modulo.md)
- [Conditionals](conditionals.md)

## Appears in

- [Day 5 · Python Loops](../days/Day%205%20-%20Beginner%20-%20Python%20Loops/Day%205%20-%20Beginner%20-%20Python%20Loops.md): `for` over a list, `range`, a running total, a running maximum, FizzBuzz, and the password generator
