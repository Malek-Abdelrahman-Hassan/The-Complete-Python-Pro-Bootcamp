---
tags:
  - concept
aliases:
  - Functions
  - def
  - return
  - Parameter
  - Argument
created: 2026-11-18
---

# Functions

## What it is

A function is a named block of code. `def` defines it once; writing its name with parentheses **calls** it, which runs the block. A function can take inputs (parameters) and hand back an output (`return`).

## Why it matters

Steps that repeat get one readable name instead of being copied. Inputs let one function handle many cases, and outputs let functions be chained together.

## Syntax

```python
def greet():                      # no inputs, no output
    print("Hello")

def greet_with(name, location):   # parameters: name, location
    print(f"Hello {name} from {location}")

def add(n1, n2):
    """Return the sum of n1 and n2."""   # docstring
    return n1 + n2                # output

greet()                           # call
greet_with("Ana", "Lisbon")       # positional arguments
greet_with(location="Lisbon", name="Ana")   # keyword arguments
total = add(2, 3)                 # the call is replaced by 5
```

The **parameter** is the name in the `def` line (`name`). The **argument** is the value passed in the call (`"Ana"`).

## Examples

```python
def turn_right():                 # Reeborg's World: three lefts make a right
    turn_left()
    turn_left()
    turn_left()

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."   # early return
    return f"{f_name.title()} {l_name.title()}"

operations = {"+": add}           # store the function, no parentheses
operations["+"](4, 8)             # call it later: 12
```

## Gotchas

> [!WARNING]
> A function that prints its result instead of returning it gives `None` to the caller. `answer = f()` then holds `None`.

- Defining a function runs nothing. Only a call with `()` runs the body.
- Code after `return` never runs.
- Swapped positional arguments land in the wrong parameters without any error. Keyword arguments avoid that.
- Call a function only after its `def` line has run, or Python raises `NameError`.
- A parameter with the same name as a variable outside the function *shadows* it. It works, but it is confusing.

## Related

- [Loops](loops.md)
- [Dictionaries](dictionaries.md)
- [Modules](modules.md)
- [PEP 8](pep-8.md)

## Appears in

- [Day 6 · Python Functions & Karel](../days/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel/Day%206%20-%20Beginner%20-%20Python%20Functions%20&%20Karel.md): `def`, calling, and `turn_right()` / `jump()` in Reeborg's World
- [Day 8 · Function Parameters & Caesar Cipher](../days/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher/Day%208%20-%20Beginner%20-%20Function%20Parameters%20&%20Caesar%20Cipher.md): parameters, arguments, positional and keyword arguments, `caesar()`
- [Day 9 · Dictionaries, Nesting and the Secret Auction](../days/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction.md): a function that takes the bids dictionary and prints the winner
- [Day 10 · Functions with Outputs](../days/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs.md): `return`, `None`, docstrings, functions stored in a dictionary, recursion
