---
tags:
  - concept
aliases:
  - Data types
  - Primitive types
  - int
  - float
  - bool
created: 2026-11-08
---

# Data types

## What it is

A data type is the kind of value Python is storing: text (`str`), whole numbers (`int`), numbers with a decimal point (`float`), or true/false (`bool`). Every value has exactly one type, and the type controls which operations are allowed.

## Why it matters

Functions expect specific types. `len()` works on strings but not on integers; `+` adds numbers but joins strings. Knowing types explains `TypeError` messages and tells you when to convert values.

## Syntax

```python
"text"           # str: string
42               # int: integer (whole number)
3.14             # float: floating point number
True             # bool: boolean (True or False, capitalised)
False
1_000_000        # int with underscores for readability (ignored by Python)
```

Check a value's type:

```python
type("hello")    # <class 'str'>
type(3)          # <class 'int'>
```

## Examples

```python
print(123 + 345)       # 468: maths on integers
print("123" + "345")   # 123345: concatenation on strings

print(6 / 3)   # 2.0: true division always returns a float
print(6 // 3)  # 2: floor division, drops the decimal part

print(2 ** 3)  # 8: exponent (2³)
```

```text
468
123345
2.0
2
8
```

## Gotchas

> [!WARNING]
> Quotes turn digits into text. `"123" + "456"` joins strings; it does not add 123 and 456.

- `True` and `False` are capitalised and have no quotes.
- In Python 3, `/` always produces a float, even when the result is a whole number.
- `//` divides then floors: `5 // 3` is `1`, not `2`.
- Integer literals can use underscores: `1_000_000` equals `1000000`.
- Mixing types with `+` usually raises `TypeError`, for example `3 + "3"`.

## Related

- [Type conversion](type-conversion.md)
- [Strings](strings.md)
- [F-strings](f-strings.md)
- [Errors and debugging](errors-and-debugging.md)

## Appears in

- [Day 2 · Understanding Data Types and How to Manipulate Strings](../days/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings.md): `str`, `int`, `float`, `bool`, arithmetic and operator precedence
