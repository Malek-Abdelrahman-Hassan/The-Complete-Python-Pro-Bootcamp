"""Coding Exercise 7 - Life in Weeks

Write life_in_weeks(age). It prints how many weeks are left until age 90,
in exactly this format, full stop included:

    You have x weeks left.

Use 52 weeks per year. Example: life_in_weeks(56) prints
    You have 1768 weeks left.

The Udemy checker has no console, so call the function with a fixed value
instead of input(). The function name must stay life_in_weeks.

Practises: a function with one parameter, arithmetic, f-strings.
"""

# Write your solution below this line.
def life_in_weeks(age):
    remaining_years = 90 - age
    remaining_weeks = remaining_years * 52
    print(f"You have {remaining_weeks} weeks left.")

life_in_weeks(20)