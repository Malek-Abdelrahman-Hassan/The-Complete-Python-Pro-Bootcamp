"""Day 1 Project - Band Name Generator

Ask for the city the user grew up in and the name of a pet, then combine the
two answers into a band name.

Example run:
    Welcome to the Band Name Generator.
    Which city did you grow up in?
    Cairo
    What is the name of a pet?
    Max
    Your band name could be Cairo Max

Requirements:
    - The cursor waits on a new line below each question.
    - The band name is the city, a space, then the pet name.

Run from this day's folder:
    python project/main.py
"""

# 1. Greet the user.

# 2. Ask which city the user grew up in and store the answer in a variable.

# 3. Ask for the name of a pet and store the answer in a variable.

# 4. Combine the city and the pet name and print the band name.
print("Welcome to the Band Name Generator.\n")
city = input("What's the name of the city you grew up in?\n")
pet = input("What is your pet's name? \n")

print("Your band name could be" + city + " " + pet)