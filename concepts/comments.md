---
tags:
  - concept
aliases:
  - Comment
created: 2026-09-26
---

# Comments

## What it is

A comment is text in a code file that Python ignores. It starts with `#` and runs to the end of the line.

## Why it matters

Comments explain code to people, including the future self who has forgotten how it works. Commenting out a line also switches it off without deleting it, which helps while testing and debugging.

## Syntax

```python
# A comment on its own line
print("Hello")  # A comment after code
```

## Examples

```python
# input() runs first, then the strings are joined, then print() shows the result.
print("Hello " + input("What is your name? ") + "!")

# print("This line is switched off")
```

## Gotchas

> [!TIP]
> `Ctrl + /` (`Cmd + /` on macOS) comments or uncomments the selected lines in most code editors, including PyCharm and VS Code.

- A `#` inside a string is just text: `print("#1")` prints `#1`.
- Good comments explain why the code does something; the code already shows what it does.
- Documentation strings for functions are covered on Day 10.

## Related

- [PEP 8](pep-8.md)

## Appears in

- [Day 1 · Working with Variables in Python to Manage Data](../days/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data.md): writing notes in code and commenting lines out
