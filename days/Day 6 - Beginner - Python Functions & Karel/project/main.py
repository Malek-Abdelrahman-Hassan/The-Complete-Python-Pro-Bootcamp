"""Day 6 Project - Escaping the Maze (Reeborg's World)

The robot starts on a random square, facing a random direction. Get it to
the exit by following the right-hand wall:

    1. If the right is clear, turn right and move.
    2. Otherwise, if the front is clear, move.
    3. Otherwise, turn left.

Repeat until at_goal() is True.

World: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Commands: move(), turn_left().
Conditions: at_goal(), front_is_clear(), right_is_clear(), wall_in_front(),
wall_on_right().

Paste this file into Reeborg's World and click Play. The commands exist only
there, so `python project/main.py` raises NameError.

Optional: some starts loop forever (step count above 1000). Make the code
escape from every start, including the course's three problem worlds.
"""

# Write your solution below this line.


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
