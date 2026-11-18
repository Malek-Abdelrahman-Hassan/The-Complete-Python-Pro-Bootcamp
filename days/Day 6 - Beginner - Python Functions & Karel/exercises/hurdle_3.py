"""Reeborg's World - Hurdle 3

Walls are placed at random, and so is their number. Follow the dotted path:
jump over a wall, otherwise move forward. Going over the top of every
hurdle in one pass does not count.

World: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

Useful conditions: at_goal(), front_is_clear(), wall_in_front().
Paste this file into Reeborg's World; it does not run with `python`.

Practises: while with if/else inside, adjusting a function.
"""

# Write your solution below this line.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
