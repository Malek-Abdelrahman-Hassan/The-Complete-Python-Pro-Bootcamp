---
tags:
  - concept
aliases:
  - Type casting
  - Type conversion
  - Casting
created: 2026-11-08
---

# Type conversion

## What it is

Type conversion (also called type casting) turns a value from one data type into another using functions such as `int()`, `float()`, `str()` and `bool()`. Checking the type first uses `type()`.

## Why it matters

`input()` always returns a string, but math needs numbers. Converting types is how programs turn typed answers into values Python can calculate with, and how numbers become text again for printing with `+`.

## Syntax

```python
int("42")        # string to integer
float("3.14")    # string to float
str(100)         # number to string
bool(1)          # truthy value to bool
type(value)      # reports the type, does not convert
```

## Examples

```python
bill = "124.56"
bill = float(bill)

tip = "12"
tip = int(tip)

length = len("Ada")
message = "Letters in your name: " + str(length)
print(message)
```

```text
Letters in your name: 3
```

## Gotchas

> [!WARNING]
> Not every string can become a number. `int("abc")` raises `ValueError: invalid literal for int() with base 10: 'abc'`.

- `int("3.9")` also fails; use `float()` first, then `int()` if a whole number is needed.
- `int()` floors toward zero; `round()` rounds to the nearest whole number.
- Converting a float to `int` chops off decimal places; it does not round.
- `bool("False")` is `True` because any non-empty string is truthy; only `bool("")` is `False`.

## Related

- [Data types](data-types.md)
- [Input and output](input-and-output.md)
- [F-strings](f-strings.md)
- [Errors and debugging](errors-and-debugging.md)

## Appears in

- [Day 2 · Understanding Data Types and How to Manipulate Strings](../days/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings.md): `type()`, converting `input()` answers, fixing `TypeError` when joining strings and numbers
