"""Day 9 Project - Secret Auction

Each bidder types a name and a bid in turn, without seeing the others.
When nobody else wants to bid, print the highest bidder.
Target: https://appbrewery.github.io/python-day9-demo/

Steps:

1. Print art.logo.
2. Ask "What is your name?: " and "What is your bid?: $". Convert the bid
   to an int.
3. Store each bid in a dictionary, name as key and bid as value. Create
   the dictionary before the loop so bids accumulate.
4. Ask "Are there any other bidders? Type 'yes' or 'no'." On "yes", hide
   the previous bid with print("\n" * 100) and loop again.
5. On "no", call a function that loops over the dictionary, keeps the
   highest bid and its name, and prints:
       The winner is Jenny with a bid of $121

Do it without max() first; the loop is the point of the exercise.

Run from this day's folder:
    python project/main.py
"""

# Write your solution below this line.

import art


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(art.logo)

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 100)