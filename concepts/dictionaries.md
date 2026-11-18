---
tags:
  - concept
aliases:
  - Dictionaries
  - Dictionary
  - dict
  - Nesting
created: 2026-11-18
---

# Dictionaries

## What it is

A dictionary stores **key: value** pairs inside curly braces. You look a value up by its key instead of by a position, the way a word leads to its definition.

## Why it matters

Related data stays labelled: a name and its bid, a student and a grade, an operator and its function. Nesting lists and dictionaries inside each other holds more complex records.

## Syntax

```python
bids = {"Ana": 120, "Ben": 95}    # create
bids["Ana"]                       # 120: read by key
bids["Cy"] = 140                  # add a new key
bids["Ben"] = 100                 # replace an existing value
empty = {}                        # empty dictionary
bids = {}                         # wipe it

for name in bids:                 # loops over the keys
    print(name, bids[name])
```

A long dictionary is written one entry per line, indented, each line ending with a comma.

## Examples

```python
student_scores = {"Harry": 88, "Neville": 60}
student_grades = {}
for student in student_scores:
    if student_scores[student] > 70:
        student_grades[student] = "Pass"
    else:
        student_grades[student] = "Fail"

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],                 # list as a value
    "Germany": {"cities_visited": ["Berlin", "Stuttgart"]},  # dictionary as a value
}
travel_log["France"][1]                       # "Lille"
travel_log["Germany"]["cities_visited"][1]    # "Stuttgart"
```

## Gotchas

> [!WARNING]
> Reading a key that does not exist raises `KeyError`. Check spelling, case, and type: `"1"` and `1` are different keys.

- `for x in d:` gives keys, not values.
- `d[key] = value` silently replaces an existing value. It does not warn.
- String keys need quotes in the literal. `{Bug: "..."}` looks for a variable called `Bug`.
- Each key holds one value. To store several, make that value a list.

## Related

- [Lists](lists.md)
- [Loops](loops.md)
- [Functions](functions.md)
- [Errors and debugging](errors-and-debugging.md)

## Appears in

- [Day 9 · Dictionaries, Nesting and the Secret Auction](../days/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction/Day%209%20-%20Beginner%20-%20Dictionaries,%20Nesting%20and%20the%20Secret%20Auction.md): creating, editing, looping, `KeyError`, nesting, and the bids dictionary
- [Day 10 · Functions with Outputs](../days/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs/Day%2010%20-%20Beginner%20-%20Functions%20with%20Outputs.md): a dictionary that maps operator symbols to functions
