"""Coding Exercise 8 - Love Calculator

Write calculate_love_score(name1, name2). Count, across both names, how
many times the letters of TRUE appear, then the letters of LOVE. Put the
two counts side by side as a two-digit number and print it.

    "Angela Yu" and "Jack Bauer"
    T 0 + R 1 + U 2 + E 2 = 5
    L 1 + O 0 + V 0 + E 2 = 3
    Love score: 53

calculate_love_score("Kanye West", "Kim Kardashian") prints 42.

Upper and lower case count the same. The Udemy checker has no console, so
call the function with fixed names instead of input().

Practises: two parameters, .lower(), .count() or a loop, string joining.
"""

# Write your solution below this line.
def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_count = 0
    love_count = 0
    for letter in name1:
        if letter in 'true':
            true_count += 1
        if letter in 'love':
            love_count += 1
    for letter in name2:
        if letter in 'true':
            true_count += 1
        if letter in 'love':
            love_count += 1
    love_score = int(str(true_count) + str(love_count))
    print(f"Your love score is {love_score}.")

calculate_love_score("Angela Yu", "Jack Bauer")