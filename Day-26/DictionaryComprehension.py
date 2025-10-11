# Dictionary Comprehension:
#   From a List -> new_dict = {new_key:new_value for item in list}
#   From a Dictionary -> new_dict = {new_key:new_value for (key, value) in old_dict.items()}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {students: random.randint(1,100) for students in names}
print(students_scores)

passed_students = {students:scores for (students, scores) in students_scores.items() if scores>=60 }
print(passed_students)