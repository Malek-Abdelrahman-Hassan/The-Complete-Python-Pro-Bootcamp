"""Reeborg's World - Hurdle 4

Walls have random positions, a random count, and now a random height.
The jump has to climb as high as each wall needs, then come back down.
The course solution fits in about 24 lines.

World: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

Useful conditions: at_goal(), front_is_clear(), wall_in_front(),
right_is_clear(), wall_on_right().
Paste this file into Reeborg's World; it does not run with `python`.

Practises: while loops inside a function, conditions.
"""

# Write your solution below this line.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
