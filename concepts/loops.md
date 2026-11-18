---
tags:
  - concept
aliases:
  - Loops
  - for loop
  - while loop
  - range
created: 2026-11-18
---

# Loops

## What it is

A loop repeats a block of code. A `for` loop runs once for every item in a collection, or once for every integer `range` produces. A `while` loop runs for as long as its condition stays true.

## Why it matters

Adding fifty scores by hand is a new line per score. A loop is one block that works for a list of any length, or keeps a game going until the player wins.

## Syntax

```python
for fruit in ["apple", "peach", "pear"]:
    print(fruit)               # once per item

for char in "camel":
    print(char)                # strings loop one character at a time

for number in range(1, 11):
    print(number)              # 1 through 10; 11 is not included

for number in range(1, 11, 3):
    print(number)              # 1, 4, 7, 10

count = 3
while count > 0:               # tested before every pass
    print(count)
    count -= 1                 # 3, 2, 1, then 0 > 0 is false
```

Lines indented under `for` or `while` repeat. A line at the same indent as the loop, written below it, runs once after the last pass.

| Use | When |
| --- | --- |
| `for` | You need each item of a list or string, or each number of a range |
| `while` | You only know when to stop, not how many passes it takes |

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

game_over = False
while not game_over:           # a flag ends the loop from inside
    guess = input("Guess: ")
    if guess == "a":
        game_over = True
```

`range` by itself prints nothing useful. The loop is what pulls each number out.

## Gotchas

> [!WARNING]
> A `while` condition that never becomes false is an **infinite loop**. Make sure something inside the body changes what the condition tests.

- `range(1, 100)` stops at 99. To include 100, the stop is 101.
- Printing an accumulator inside the loop shows every partial result. Print it after the loop when only the final value matters.
- A list or string that must survive between passes is created before the loop, not inside it.
- A loop body that is not indented raises `IndentationError`.

## Related

- [Lists](lists.md)
- [Random](random.md)
- [Modulo](modulo.md)
- [Conditionals](conditionals.md)
- [Functions](functions.md)
- [Dictionaries](dictionaries.md)

## Appears in

- [Day 5 · Python Loops](../days/Day%205%20-%20Beginner%20-%20Python%20Loops/Day%205%20-%20Beginner%20-%20Python%20Loops.md): `for` over a list, `range`, a running total, a running maximum, FizzBuzz, and the password generator
- [Day 6 · Python Functions & Karel](../days/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel.md): `while`, `while not at_goal()`, `for` versus `while`, and infinite loops
- [Day 7 · Hangman](../days/Day%207%20-%20Beginner%20-%20Hangman/Day%207%20-%20Beginner%20-%20Hangman.md): `for` over a string, `range(len(word))`, and `while not game_over`
- [Day 8 · Function Parameters & Caesar Cipher](../days/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher.md): building the shifted text letter by letter, and `while should_continue`
- [Day 9 · Dictionaries, Nesting and the Secret Auction](../days/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction.md): looping over a dictionary's keys and finding the highest bid
- [Day 10 · Functions with Outputs](../days/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs.md): a `while` loop that keeps calculating with the previous answer
