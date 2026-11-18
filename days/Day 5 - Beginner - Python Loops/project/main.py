"""Day 5 Project - Password Generator

Ask three questions, then build two passwords from fresh random picks.

Easy: letters, then symbols, then numbers, in that order.
Hard: its own list of letters, symbols, and numbers, shuffled, then joined.
The hard password does not reuse the easy string.

random.choice(sequence) picks one item.
random.shuffle(items) reorders that list and returns None. Join the list
into a string after the shuffle.

Run from this day's folder:
    python project/main.py
"""

import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy: letters, then symbols, then numbers. Its own random picks.
easy_password = ""
for _ in range(nr_letters):
    easy_password += random.choice(letters)
for _ in range(nr_symbols):
    easy_password += random.choice(symbols)
for _ in range(nr_numbers):
    easy_password += random.choice(numbers)
print(f"Easy password: {easy_password}")

# Hard: a separate list, shuffled, then joined. Not built from easy_password.
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")