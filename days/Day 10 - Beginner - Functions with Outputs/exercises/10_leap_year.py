"""Coding Exercise 10 - Leap Year

Write is_leap_year(year). It returns True or False, the booleans, not the
strings.

A year is a leap year when:
    it divides by 4 with no remainder,
    except when it also divides by 100,
    unless it also divides by 400.

    2000 -> True     (divides by 400)
    2100 -> False    (divides by 100, not by 400)
    2400 -> True
    1989 -> False

Keep the function name. The Udemy checker has no console, so call the
function with a fixed year and print what it returns.

Practises: return, nested if or and/or, modulo.
"""


def is_leap_year(year):
    # Write your solution below this line.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(2000))
print(is_leap_year(2100))
print(is_leap_year(2400))
print(is_leap_year(1989))