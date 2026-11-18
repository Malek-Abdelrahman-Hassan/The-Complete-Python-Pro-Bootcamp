"""Highest Score

The lesson list of exam scores adds up to 2068. Its largest score is 199.
Do not call max() or sum(). Find the largest score with a for loop.

Practises: for, a variable updated inside the loop, if.
"""

student_scores = [
    150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89,
]
highest_score = 0
# Write your solution below this line.
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)
