"""Coding Exercise 9 - Grading Program

student_scores maps each student's name to an exam score. Build a new
dictionary, student_grades, that maps the same names to a grade:

    91 - 100    "Outstanding"
    81 - 90     "Exceeds Expectations"
    71 - 80     "Acceptable"
    70 or lower "Fail"

Do not change student_scores. The checker reads the final student_grades.
Expected result:

    {'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable',
     'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}

Practises: looping over a dictionary, adding keys, if/elif/else.
"""

student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60,
}

# Write your solution below this line.
student_grades = {}
for student in student_scores: 
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)