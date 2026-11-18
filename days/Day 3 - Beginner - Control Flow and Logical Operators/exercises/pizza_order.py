"""Pizza Order Practice

This is the challenge in the Pizza Order lesson, not a separate numbered coding exercise.

Three inputs are already collected: size, pepperoni, and extra_cheese.
Print the final bill.

Prices:
    S = 15, M = 20, L = 25
    Pepperoni: +2 on a small, +3 on a medium or large
    Extra cheese: +1 on any size

Example:
    What size pizza do you want? S, M or L: L
    Do you want pepperoni on your pizza? Y or N: Y
    Do you want extra cheese? Y or N: N
    Your final bill is: $28.

Practises: if/elif/else, a nested if, and a later if that adds with +=.
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Write your solution below this line.
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
