"""Reeborg's World - Hurdle 2

The flag is placed at random, so the number of hurdles changes each run.
Keep jumping until the robot stands on the flag.

World: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

Useful condition: at_goal() is True on the flag.
Paste this file into Reeborg's World; it does not run with `python`.

Practises: while, not.
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


while not at_goal():
    jump()
