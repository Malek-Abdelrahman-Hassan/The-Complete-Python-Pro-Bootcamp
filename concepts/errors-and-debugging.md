---
tags:
  - concept
aliases:
  - Debugging
  - Error messages
  - Traceback
created: 2026-09-26
---

# Errors and debugging

## What it is

When Python cannot run a line of code, it stops and prints an error report called a **traceback**. **Debugging** is the process of finding and fixing the cause.

## Why it matters

Every programmer makes mistakes. Being good at programming largely means being quick at reading error messages and working out what caused them.

## Reading an error

```text
  File "main.py", line 1          <- which file and which line
    print("Hello world!)          <- the code on that line
          ^                       <- where Python got confused
SyntaxError: unterminated string literal (detected at line 1)
                                  <- the error type and what went wrong
```

Read from the bottom up: the last line gives the error type and message, the lines above it point to the place.

## Common errors

| Error | Meaning | Typical cause |
| --- | --- | --- |
| `SyntaxError` | The code breaks Python's grammar rules | A missing quote or parenthesis, curly quotes, a name starting with a digit |
| `IndentationError` | Unexpected or missing spaces at the start of a line | A stray space or tab before a line |
| `NameError` | The code uses a name Python does not know | A typo, the wrong capital letters, or a variable used before it is created |
| `TypeError` | An operation does not work on these types | `len(123)`, mixing `str` and `int` with `+`, passing the wrong type to a function |
| `ValueError` | The type is right but the value is invalid | `int("abc")` when the string is not a number |
| `IndexError` | An index does not exist in the sequence | `items[len(items)]` — the last index is `len(items) - 1` |

`SyntaxError` and `IndentationError` are found before the program starts, so nothing runs. A `NameError` only appears when Python reaches the faulty line.

## How to debug

1. Run the code and read the last line of the error.
2. Go to the line number it reports. The actual mistake is sometimes on the line just before it.
3. Check the colours: syntax highlighting shows where a string or bracket was left open.
4. Fix one error, then run again.
5. If the message is unclear, search for its last line; beginner errors are almost always explained online.
6. To see what Python does step by step, use a debugger such as the one in [Thonny](https://thonny.org) or PyCharm.

> [!NOTE]
> Editor underlines (red for errors, yellow for warnings) depend on the editor. Error messages come from Python itself and are the same everywhere.

## Gotchas

- Fix errors from the top down: one mistake can cause misleading errors further down.
- Code that runs is not necessarily correct. `print("Hello" + name)` runs but prints no space, so compare the output with what was expected.

## Related

- [PEP 8](pep-8.md)
- [Variables](variables.md)
- [Strings](strings.md)

## Appears in

- [Day 1 · Working with Variables in Python to Manage Data](../days/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data.md): `SyntaxError`, `IndentationError`, `NameError` and fixing errors from the messages alone
- [Day 2 · Understanding Data Types and How to Manipulate Strings](../days/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings.md): `TypeError` and `ValueError` from wrong types and invalid conversions
- [Day 3 · Control Flow and Logical Operators](../days/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators.md): `IndentationError` when an `if` block is not indented, and `SyntaxError` from using `=` instead of `==`
- [Day 4 · Randomisation and Python Lists](../days/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists.md): `IndexError: list index out of range` from an off-by-one index
- [Day 5 · Python Loops](../days/Day%205%20-%20Beginner%20-%20Python%20Loops/Day%205%20-%20Beginner%20-%20Python%20Loops.md): `IndentationError` when the body of a `for` loop is not indented
