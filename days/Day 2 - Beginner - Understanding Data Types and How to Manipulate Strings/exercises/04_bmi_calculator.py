"""Coding Exercise 4 - BMI Calculator

Calculate BMI from weight and height, then print the result as a whole number.

BMI = weight (kg) / height (m) ** 2

See the full brief in _raw/Coding Exercise 4 BMI Calculator.md (local only).

Example output (height 1.75, weight 80):
    26
"""

# Do not change the code below this line.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Write your code below this line.
BMI = int(weight) / float(height) ** 2
print(round(BMI, 2)) # round() is used to round the BMI to 2 decimal places