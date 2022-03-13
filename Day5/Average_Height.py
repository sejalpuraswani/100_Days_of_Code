#Program to calculate the average height of students

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#this will give total height of all students
total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height is: {total_height}")


#It will give total number of students
total_number_Students = 0
for student in student_heights:
    total_number_Students += 1
print(f"Total number of Students is: {total_number_Students}")


#calculates the average height of students
average_height = round(total_height / total_number_Students)
print(f"Average height is: {average_height}")
