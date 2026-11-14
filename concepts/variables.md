---
tags:
  - concept
aliases:
  - Variable
  - Assignment
created: 2026-09-26
---

# Variables

## What it is

A variable is a name that refers to a value. Like a labelled box, the name is the label and the value is what is stored inside.

## Why it matters

Variables let a program remember data, such as a user's answer, and use it again later. Code written with variable names works with any value, not just one fixed piece of text.

## Syntax

```python
variable_name = value   # assignment: store value under variable_name
variable_name = other   # reassignment: replace the stored value
```

`=` means assignment, not "is equal to". Comparing values is covered on Day 3.

## Examples

```python
city = input("Which city did you grow up in?\n")
print("You grew up in " + city)

name = "Jack"
print(name)
name = "Ada"
print(name)

# A variable can hold the result of a function
length = len(name)
print(length)
```

```text
Which city did you grow up in?
Cairo
You grew up in Cairo
Jack
Ada
3
```

## Naming rules

| Rule | Valid | Invalid |
| --- | --- | --- |
| Only letters, digits and underscores | `user_name` | `user name`, `user-name` |
| Must not start with a digit | `place_1` | `1st_place` |
| Must not be a keyword | `class_name` | `class`, `if`, `for` |

Conventions from [PEP 8](pep-8.md):

- Lowercase words joined by underscores (`snake_case`): `pet_name`, not `petName`.
- Descriptive names: `city` rather than `c`.
- No names of built-in functions such as `print` or `input`.

## Gotchas

> [!WARNING]
> Names are case-sensitive. `print(User_name)` after `user_name = "Ada"` raises `NameError: name 'User_name' is not defined. Did you mean: 'user_name'?`

- Using a variable before assigning it raises a `NameError`.
- Python does not check spelling, only that names match: `nama` is a valid name if it is used consistently. Editor spell-check squiggles are not errors.
- Assigning to a built-in name such as `print` works, but the function is then gone: the next `print()` raises `TypeError: 'str' object is not callable`.
- Reassigning replaces the old value completely. To keep it, copy it into another variable first.

## Related

- [Input and output](input-and-output.md)
- [Strings](strings.md)
- [Errors and debugging](errors-and-debugging.md)

## Appears in

- [Day 1 · Working with Variables in Python to Manage Data](../days/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data.md): assignment, reassignment and naming rules
