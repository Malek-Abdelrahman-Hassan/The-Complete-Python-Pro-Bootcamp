---
tags:
  - concept
aliases:
  - List
  - Lists
  - Index
created: 2026-11-18
---

# Lists

## What it is

A list stores many values, in order, under one name. Each value is an item. Its position is an **index**, also called an offset from the start.

## Why it matters

Separate variables (`state1`, `state2`) do not scale. A list can grow, be looped over, and be picked from at random.

## Syntax

```python
fruits = ["Cherry", "Apple", "Pear"]
fruits[0]          # "Cherry" — the first item is index 0
fruits[-1]         # "Pear" — negative indexes count from the end
len(fruits)        # 3
fruits.append("Lime")          # one new item at the end
fruits.extend(["Fig", "Plum"]) # each item added, not a list inside a list

outer = [["a", "b"], ["c"]]
outer[0][1]        # "b"
```

The last valid index is `len(fruits) - 1`. Index `len(fruits)` raises `IndexError: list index out of range`.

## Examples

```python
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[0])                 # Alice
print(friends[len(friends) - 1])  # Emanuel
```

A list of lists keeps two groups together. `dirty_dozen[1][0]` is the first item of the second inner list.

## Gotchas

> [!WARNING]
> `append([1, 2])` adds a single item, and that item is a list. `extend([1, 2])` adds `1` and then `2`.

- Counting from 1 instead of 0 reads the wrong item and, at the end, raises `IndexError`.
- `len` is the count, not the last index.

## Related

- [Random](random.md)
- [Loops](loops.md)
- [Errors and debugging](errors-and-debugging.md)
- [Strings](strings.md)

## Appears in

- [Day 4 · Randomisation and Python Lists](../days/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists/Day%204%20-%20Beginner%20-%20Randomisation%20and%20Python%20Lists.md): indexes, `append`, `extend`, nested lists, and `IndexError`
- [Day 5 · Python Loops](../days/Day%205%20-%20Beginner%20-%20Python%20Loops/Day%205%20-%20Beginner%20-%20Python%20Loops.md): looping over a list, and a list of password characters that gets shuffled
