---
tags:
  - concept
aliases:
  - String
  - str
created: 2026-09-26
---

# Strings

## What it is

A string is a sequence of characters, such as a word, a sentence or an empty piece of text. It is Python's type for text, written between matching quotes.

## Why it matters

Nearly every program works with text: messages, names, user input and file contents. Everything `input()` returns is a string.

## Syntax

```python
"double quotes"
'single quotes'
"Line 1\nLine 2"     # \n starts a new line
"Hello" + " world"   # + joins (concatenates) strings
len("Hello")         # 5: the number of characters
"hello"[0]           # subscripting: character at index 0 (first is 0)
"hello"[-1]          # last character
"Left".lower()       # "left": a new string in lowercase
```

## Examples

```python
print("Hello" + "Ada")        # HelloAda: + adds no space
print("Hello " + "Ada")       # Hello Ada
print("Hello" + " " + "Ada")  # Hello Ada

print("Top\nMiddle\nBottom")

# Use one kind of quote around text that contains the other
print('She said "hi"')
print("It's fine")

word = "hello"
print(word[0])   # h
print(word[4])   # o
print(word[-1])  # o (last character)
```

```text
HelloAda
Hello Ada
Hello Ada
Top
Middle
Bottom
She said "hi"
It's fine
h
o
o
```

**Subscripting** picks one character by its index. Indices start at `0`. A negative index counts from the end: `-1` is the last character.

## Gotchas

> [!WARNING]
> A string must end with the same kind of quote it starts with. `print("Hi)` fails with `SyntaxError: unterminated string literal`.

- `\n` uses a backslash. `/n` is not special and is printed as it is.
- A space after `\n` appears at the start of the next line.
- Quotes copied from word processors (`“` and `”`) are not valid Python quotes: `SyntaxError: invalid character '“' (U+201C)`.
- Only strings can be joined with `+`; `"a" + 1` raises `TypeError`. Convert the number with `str()` or use an [f-string](f-strings.md).
- `.lower()` returns a new string; it does not change the original unless the result is stored: `choice = choice.lower()`.
- An index that is too large raises `IndexError: string index out of range`.

## Related

- [Input and output](input-and-output.md)
- [Variables](variables.md)

## Appears in

- [Day 1 · Working with Variables in Python to Manage Data](../days/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data/Day%201%20-%20Beginner%20-%20Working%20with%20Variables%20in%20Python%20to%20Manage%20Data.md): string literals, `\n`, concatenation with `+` and `len()`
- [Day 2 · Understanding Data Types and How to Manipulate Strings](../days/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings/Day%202%20-%20Beginner%20-%20Understanding%20Data%20Types%20and%20How%20to%20Manipulate%20Strings.md): subscripting and indexing from zero
- [Day 3 · Control Flow and Logical Operators](../days/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators/Day%203%20-%20Beginner%20-%20Control%20Flow%20and%20Logical%20Operators.md): `.lower()` so `"Left"` and `"left"` compare as equal
- [Day 7 · Hangman](../days/Day%207%20-%20Beginner%20-%20Hangman/Day%207%20-%20Beginner%20-%20Hangman.md): looping over a word, building `display` with `+=`, and `in` / `not in`
- [Day 10 · Functions with Outputs](../days/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs.md): `.title()` returns a title-cased copy of a name
