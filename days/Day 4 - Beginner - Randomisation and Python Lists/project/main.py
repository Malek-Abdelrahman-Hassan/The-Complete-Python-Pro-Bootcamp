"""Day 4 Project - Rock Paper Scissors

The player types 0, 1, or 2. The computer picks one of those at random.
Print both shapes, then the result.

    0 rock, 1 paper, 2 scissors
    Rock beats scissors.
    Scissors beats paper.
    Paper beats rock.
    The same number: It's a draw.

input() is a string. Convert it with int() before comparing it to a number.
A higher number is not always the winner: rock is 0 and still beats scissors (2).

The course starter stores an ASCII picture in rock, paper, and scissors.
Paste those pictures from the lesson over the placeholders below.

Run from this day's folder:
    python project/main.py
"""

import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

# Ask: What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
# Store the answer as an int. A newline at the end of the prompt puts the
# cursor on the next line.

# Computer choice: random.randint(0, 2)

# Print the picture for the player, then the picture for the computer.

# Print "You win", "You lose", or "It's a draw."
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)
if player_choice == 0:
    print("""
    _______
----'   ____)
      (_____)
      (_____)
      (____)
----.__(___)
    """)
elif player_choice == 1:
    print("""
    _______
----'   ____)_____
          ______)
          _______)
         _______)
---.__________)
    """)
elif player_choice == 2:
    print("""
    _______
----'   ____)______
          ______)
       __________)
      (____)
----.__(___)
    """)
else: 
    print("Invalid choice. Please try again.")
if computer_choice == 0:
    print("""
    _______
----'   ____)
      (_____)
      (_____)
      (____)
----.__(___)
    """)
elif computer_choice == 1:
    print("""
    _______
----'   ____)_____
          ______)
          _______)
         _______)
---.__________)
    """)
elif computer_choice == 2:
    print("""
    _______
----'   ____)______
          ______)
       __________)
      (____)
----.__(___)
    """)  
if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 1 and computer_choice == 0:
    print("You win!")
elif player_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")