---
tags:
  - concept
aliases:
  - f-string
  - Formatted string
  - f"..."
created: 2026-11-08
---

# F-strings

## What it is

An f-string is a string literal with an `f` before the opening quote. Placeholders inside curly braces `{ }` are replaced by the values of variables or expressions, and Python converts them to text automatically.

## Why it matters

Building messages with many `+` signs and `str()` calls is slow to write and easy to get wrong. F-strings let one sentence mix text with numbers, floats and booleans without manual conversion.

## Syntax

```python
name = "Ada"
score = 10
print(f"Hello, {name}! Your score is {score}.")
```

Expressions are allowed inside the braces:

```python
print(f"Half of 10 is {10 / 2}.")
```

## Examples

```python
score = 0
height = 1.8
is_winning = True
print(f"Score: {score}, height: {height} m, winning: {is_winning}")
```

```text
Score: 0, height: 1.8 m, winning: True
```

```python
amount = 19.934285
print(f"Each person should pay: ${amount:.2f}")
```

```text
Each person should pay: $19.93
```

> [!NOTE]
> Formatting like `:.2f` (two decimal places) is introduced in more detail later in the course. For Day 2, `round(amount, 2)` inside the braces works too: `f"{round(amount, 2)}"`.

## Gotchas

> [!WARNING]
> The `f` must come **before** the opening quote: `f"text"`, not `"f{text}"`.

- Curly braces in the literal text must be doubled: `f"{{not a variable}}"`.
- Without the `f` prefix, `{score}` is printed literally, not replaced.
- F-strings are available in Python 3.6+.

## Related

- [Strings](strings.md)
- [Type conversion](type-conversion.md)
- [Input and output](input-and-output.md)

## Appears in

- [Day 2 · Understanding Data Types and How to Manipulate Strings](../days/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings.md): printing the tip calculator result without chaining `str()` and `+`
