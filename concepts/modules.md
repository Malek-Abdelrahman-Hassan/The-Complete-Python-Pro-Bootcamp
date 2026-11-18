---
tags:
  - concept
aliases:
  - Modules
  - import
created: 2026-11-18
---

# Modules

## What it is

A module is a Python file whose names (variables, functions) other files can use. `import` loads it. Python ships modules such as `random`, and any `.py` file you write is a module too.

## Why it matters

Splitting a program into files keeps each one short. Long data such as word lists or ASCII art can live in its own file, out of the way of the game logic.

## Syntax

```python
import random                     # whole module: use random.choice(...)
random.randint(1, 6)

from random import choice         # one name: use choice(...) directly
choice(["a", "b"])

from hangman_art import stages, logo   # several names, comma-separated
```

For your own files, the module name is the file name without `.py`. Python finds it when it sits in the same folder as the script you run.

## Examples

```python
# hangman_words.py
word_list = ["aardvark", "baboon", "camel"]

# main.py, in the same folder
import hangman_words
print(hangman_words.word_list[0])     # aardvark

import art
print(art.logo)
```

## Gotchas

> [!WARNING]
> After `import hangman_words`, the plain name `word_list` is undefined. Write `hangman_words.word_list`, or import the name itself with `from hangman_words import word_list`.

- PEP 8 puts all imports at the top of the file.
- Naming your own file `random.py` hides the standard `random` module.

## Related

- [Random](random.md)
- [Functions](functions.md)
- [PEP 8](pep-8.md)

## Appears in

- [Day 4 · Randomisation and Python Lists](../days/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists.md): `import random` and importing a file of your own
- [Day 7 · Hangman](../days/Day%207%20-%20Beginner%20-%20Hangman/Day%207%20-%20Beginner%20-%20Hangman.md): `import hangman_words` and `from hangman_art import stages, logo`
- [Day 8 · Function Parameters & Caesar Cipher](../days/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher.md): `import art` for the logo
- [Day 9 · Dictionaries, Nesting and the Secret Auction](../days/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction.md): `import art` for the gavel
- [Day 10 · Functions with Outputs](../days/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs.md): `import art` for the calculator logo
