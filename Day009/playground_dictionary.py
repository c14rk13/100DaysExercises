# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.
# The final version of the student_grades dictionary will be checked.
#
# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary.
#
# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

score_criteria = [
    {
            "criteria": "Outstanding",
            "min": 91,
            "max": 100
    },
    {
            "criteria": "Exceeds Expectations",
            "min": 81,
            "max": 90
    },
    {
            "criteria": "Acceptable",
            "min": 71,
            "max": 80
    },
    {
            "criteria": "Fail",
            "min": 0,
            "max": 70
    },
]

student_grades = {}


def get_score_criteria(score):
    if score > 90:
        return "Outstanding"
    if score > 80:
        return "Exceeds Expectations"
    if score > 70:
        return "Acceptable"
    else:
        return "Fail"


for student in student_scores:
    student_grades[student] = get_score_criteria(student_scores[student])

for student in student_grades:
    print(f"{student} - {student_grades[student]}")