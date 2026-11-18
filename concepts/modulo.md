---
tags:
  - concept
aliases:
  - Modulo
  - Remainder
  - "%"
created: 2026-11-16
---

# Modulo

## What it is

The modulo operator `%` divides one number by another and returns the remainder.

## Why it matters

A remainder of `0` means the division was exact. That single test answers "is this even?", "does this year divide by 4?", and similar questions, which then become `if` conditions.

## Syntax

```python
print(7 % 2)    # 1
print(10 % 2)   # 0
print(13 % 5)   # 3
```

## Examples

```python
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```

A year is divisible by 4 when `year % 4 == 0`. The same pattern works for 100 and 400.

## Gotchas

> [!WARNING]
> `%` has the same precedence family as `*` and `/`. `10 + 3 % 2` is `11`, not `1`, because the remainder is calculated before the addition. Use parentheses when the grouping is not obvious.

- The test for "no remainder" is `n % d == 0`, with two equals signs.
- `%` on a float is legal but can show the same tiny rounding noise as other float maths. Day 3 uses it on integers.
- Do not confuse `%` with `/` or `//`. `/` is the quotient as a float, `//` drops the fraction, `%` keeps only the remainder.

## Related

- [Conditionals](conditionals.md)
- [Data types](data-types.md)

## Appears in

- [Day 3 · Control Flow and Logical Operators](../days/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators.md): even and odd numbers, using `number % 2 == 0`
- [Day 8 · Function Parameters & Caesar Cipher](../days/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher.md): `% len(alphabet)` wraps a shifted letter back to the start of the alphabet
- [Day 10 · Functions with Outputs](../days/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs.md): divisibility tests in the leap-year exercise
