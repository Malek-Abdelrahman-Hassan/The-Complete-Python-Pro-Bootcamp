---
tags:
  - concept
aliases:
  - Logical operators
  - and
  - or
  - not
created: 2026-11-16
---

# Logical operators

## What it is

Logical operators combine or invert conditions. `and` requires both sides to be true. `or` requires at least one side. `not` flips a single condition.

## Why it matters

A real rule is often two comparisons at once: an age between 45 and 55, a year divisible by 4 but not by 100. One comparison cannot say that.

## Syntax

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

age = 50
if age >= 45 and age <= 55:
    print("In range.")
```

`45 <= age <= 55` is the same test written as a chained comparison.

## Examples

```python
has_ticket = True
is_late = False
if has_ticket and not is_late:
    print("You may enter.")
```

```python
choice = "swim"
if choice == "swim" or choice == "wait":
    print("That is one of the lake options.")
```

## Gotchas

> [!WARNING]
> `age >= 45 or age <= 55` is true for almost every age, because every age is either at least 45 or at most 55. A closed range uses `and`.

- `and` and `or` do not compare a value to two numbers by themselves. `18 == 18 or 21` is not "18 equals 18 or 21". Each side of `or` needs to be a full condition: `age == 18 or age == 21`.
- `not` applies to one condition. `not age >= 45` is legal; read it as "not (age >= 45)". When the grouping is unclear, add parentheses.

## Related

- [Conditionals](conditionals.md)
- [Data types](data-types.md)

## Appears in

- [Day 3 · Control Flow and Logical Operators](../days/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators.md): `and`, `or`, and `not`, including the age range that gets a free ticket
- [Day 6 · Python Functions & Karel](../days/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel.md): `while not at_goal()` keeps going until the goal is reached
- [Day 10 · Functions with Outputs](../days/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs.md): combining the leap-year rules
