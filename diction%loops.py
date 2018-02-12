#creating three dictions
lloyd = {
     "name": "Lloyd",
     "homework" :[90.0, 97.0, 75.0, 92.0],
     "quizzes" :[88.0,40.0,94.0],
     "test" : [75.0, 90.0]
}

alice = {
     "name": "Alice",
     "homework" : [100.0, 92.0,98.0, 100.0],
     "quizzes" :[82.0,83.0,91.0],
     "test" : [89.0,97.0]
}

tyler = {
     "name": "Type",
     "homework" :[0.0, 87.0, 75.0, 22.0],
     "quizzes" : [0.0,75.0, 78, 78.0],
     "test" :[100.0, 100.0]
     }

students = [lloyd, alice, tyler]

for student in students:
     #DICT[KEY] ----->value
     print(student['name']) /n
     print(student['homework'])
     print(student['quizzes'])
     print(student['test'])
     

