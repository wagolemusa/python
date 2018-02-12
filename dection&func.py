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

# Add your function bellow
def average(numbers):
     total  = sum(numbers)
     total = float(total)
     return total / len(numbers)

#define function called get_average that takes one one argument called student
#make  aviable homework that store the  average() of  student ["homework"]

def get_average(student):
     homework = average(student['homework'])
     quizzes  = average(student['quizzes'])
     test     = average(student['test'])

#Multpuly the 3 averages by their weight and run the sun of those three.
# Homework is 10%
#quizzes is 30%
# test is 60 %
##
weighted_homework = homework * 0.10
weighted_quizzes  = quizzes  * 0.30
weighted_test     = test     * 0.60

return weighted_homework + weighted_quizzes + weighted_test

def get_letter_grade(score):
     if score >= 90:
          return 'A'
     elif score >= 80:
          return 'B'
     elif score >= 70:
          return 'C'
     elif score  >= 60:
          return 'D'
     else:
          return 'F'
print(get_letter_grade(get_average(lloyd)))

#Define afunction  called get_class_averrage that has one argument students.

def get_class_average(students):
     results = [] #empty list

#For each student item in the class list calcute
#get_average(student)and then call results.append() with that result
     
     for student in students:
          student_average = get_average(student)
          results.append(student_average)

#Finally return the result of calling average() with results.
     return average(results)


#print out the result of calling get_class_average with your students list
#students list your student should be [lloyd, alice, tyler]

results = get_class_average([lloyd, alice, tyler])

print(results)
print(get_letter_grade(results))






