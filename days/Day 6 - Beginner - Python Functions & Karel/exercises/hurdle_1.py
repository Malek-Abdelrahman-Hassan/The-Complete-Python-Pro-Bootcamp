"""Reeborg's World - Hurdle 1

Six identical hurdles stand between the robot and the flag. Reach the flag
with as few lines as possible while keeping the code readable.

World: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

Paste this file into Reeborg's World. move() and turn_left() exist only
there, so `python hurdle_1.py` raises NameError.

Practises: def, calling a function, for with range.
"""

# Write your solution below this line.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    jump()
