"""Who will pay the bill?

Pick one name at random from the list. Each run can print a different name.

Alice is index 0. The list has five names, so a random index runs from 0 to 4
inclusive. random.choice(friends) does the same job in one call.

The lesson shows these names. If the list on screen is different, paste that list
over this one.

Practises: random.choice, or randint plus an index.
"""

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Write your solution below this line.
print(random.choice(friends))
print(friends[random.randint(0, len(friends) - 1)])
