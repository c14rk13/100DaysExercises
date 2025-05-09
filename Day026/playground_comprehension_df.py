import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)

# For comprehension:
# {new_key: new_value for(index, row) in df.iterrows()}