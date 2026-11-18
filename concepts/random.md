---
tags:
  - concept
aliases:
  - Random
  - random module
  - randint
created: 2026-11-18
---

# Random

## What it is

The `random` module generates numbers that are not fixed in advance. They are **pseudorandom**: a formula produces them, so they are not truly unpredictable, but they are different enough for games and passwords.

## Why it matters

Without it, a game plays the same way every run. A coin toss, a random name, and a shuffled password all start with `import random`.

## Syntax

```python
import random

random.randint(1, 10)     # integer, both ends included
random.random()            # float, 0.0 included, 1.0 excluded
random.random() * 5        # float from 0.0 up to, but not including, 5.0
random.choice(items)       # one item from a list
random.shuffle(items)      # reorder items in place; returns None
```

`import random` loads the module. `random.randint` is the function inside it. A file of your own works the same way: `import my_module`, then `my_module.some_name`.

## Examples

```python
import random

toss = random.randint(0, 1)
if toss == 0:
    print("Heads")
else:
    print("Tails")

names = ["Alice", "Bob", "Charlie"]
print(random.choice(names))
```

## Gotchas

> [!WARNING]
> `randint(a, b)` can return `b`. `random()` never returns `1`. Mixing those two up shifts a range by one.

- Call `random.shuffle(items)` on its own. Assigning it (`password = random.shuffle(items)`) stores `None`.
- `import random` has to run before any `random.` call, or Python raises `NameError`.

## Related

- [Lists](lists.md)
- [Loops](loops.md)
- [Conditionals](conditionals.md)
- [Modules](modules.md)

## Appears in

- [Day 4 · Randomisation and Python Lists](../days/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists.md): `randint`, `random()`, a coin toss, `choice`, and the computer's move in Rock Paper Scissors
- [Day 5 · Python Loops](../days/Day%205%20-%20Beginner%20-%20Python%20Loops/Day%205%20-%20Beginner%20-%20Python%20Loops.md): `choice` for each password character, then `shuffle` for the hard version
- [Day 7 · Hangman](../days/Day%207%20-%20Beginner%20-%20Hangman/Day%207%20-%20Beginner%20-%20Hangman.md): `random.choice(word_list)` picks the hidden word
