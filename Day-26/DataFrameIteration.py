import pandas as pd

student_scores = {
    "students": ["Angela", "James", "Lily"],
    "scores": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_scores)
print(student_data_frame)

for (key, value) in student_data_frame.items():
    print(value)

# Looping through each row in a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.students)
    print(row.scores)