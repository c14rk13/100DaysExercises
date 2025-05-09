#Implement the max() function via a for loop

student_scores = [180, 124, 165, 173, 189, 169, 146]
highest_score = student_scores[1]

for studentScore in student_scores:
    if studentScore > highest_score:
        highest_score = studentScore

print(f"The highest score is {highest_score}")