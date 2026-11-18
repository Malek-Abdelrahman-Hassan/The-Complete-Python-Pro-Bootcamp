---
tags:
  - concept
aliases:
  - PEP8
  - Style guide
created: 2026-09-26
---

# PEP 8

## What it is

[PEP 8](https://peps.python.org/pep-0008/) is the official style guide for Python code. It describes how to lay out and name things so that Python code looks consistent from one project to another.

## Why it matters

Code is read far more often than it is written. Following one shared style makes code easier to read, and many editor warnings, such as PyCharm's yellow underlines, are PEP 8 checks.

## Rules met so far

```python
# Names: lowercase words joined by underscores (snake_case)
pet_name = "Max"

# No space between a function name and its parentheses
print("Hello")     # good
print ("Hello")    # runs, but flagged as bad style
```

- End every file with a newline, so the last line of code is followed by an empty line.

## Gotchas

> [!NOTE]
> PEP 8 warnings do not stop code from running; errors do. A warning is advice about style, not a bug.

- Editors differ in which style checks they show, but the guide itself is the same everywhere.

## Related

- [Variables](variables.md)
- [Comments](comments.md)
- [Errors and debugging](errors-and-debugging.md)

## Appears in

- [Day 1 · Working with Variables in Python to Manage Data](../days/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data.md): editor warnings, `snake_case` names and a newline at the end of a file
- [Day 6 · Python Functions & Karel](../days/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel.md): four spaces per indentation level, spaces rather than tabs
