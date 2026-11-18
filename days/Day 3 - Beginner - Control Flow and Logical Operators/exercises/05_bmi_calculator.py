"""Coding Exercise 5 - BMI Calculator with Interpretations

bmi is already calculated. Do not change weight, height, or bmi.

Print one category:
    under 18.5              underweight
    18.5 up to (not including) 25   normal weight
    25 or over              overweight

With the given numbers, bmi is about 24.8, so the category is normal weight.

Practises: if/elif/else, comparisons.
"""

weight = 85
height = 1.85
bmi = weight / (height ** 2)
# Do not modify the values above
# Write your solution below this line.
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")