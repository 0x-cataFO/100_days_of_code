student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# GET THE TOTAL HEIGHT
total_height = 0
for height in student_heights:
    total_height += height

# GET THE LENGTH OF THE LIST
number_of_students = 0
for number in student_heights:
    number_of_students += 1

# CALCULATE THE AVERAGE AND ROUND TO THE NEAREST WHOLE NUMBER
average_height = round(total_height / number_of_students)
print(average_height)
