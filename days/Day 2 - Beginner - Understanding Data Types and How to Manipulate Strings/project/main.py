"""Day 2 Project - Tip Calculator

Split a restaurant bill between friends, including a percentage tip, and show
each person's share rounded to two decimal places.

Example run:
    Welcome to the tip calculator!
    What was the total bill? $124.56
    What percentage tip would you like to give? 10, 12, or 15? 12
    How many people to split the bill? 7
    Each person should pay: $19.93

Requirements:
    - Read bill amount, tip percentage, and number of people.
    - Convert inputs to the right numeric types (float for the bill, int for tip
      and people).
    - Apply the tip, divide the total by the number of people, and round each
      share to 2 decimal places.

Run from this day's folder:
    python project/main.py
"""

# 1. Print a welcome message.

# 2. Ask for the total bill and store it as a float.

# 3. Ask for the tip percentage (whole number, no % sign) and store it as an int.

# 4. Ask how many people are splitting the bill and store it as an int.

# 5. Calculate the bill including tip, then each person's share.

# 6. Print how much each person should pay (two decimal places).
print("welcome to the tip calculator!")
bill = input("what was the total bill? $")
tip = input("what percentage tip would you like to give? 10, 12, or 15? ")
people = input("how many people are splitting the bill? ")
total_bill = float(bill) * (1 + float(tip) / 100)
each_person = total_bill / int(people)
print(f"Each person should pay: ${each_person:.2f}")