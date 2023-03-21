# WAP to read the record of n students in a dictionary containing key/value pairs of name: [marks]. Print the average of the marks obtained by the particular student correct to 2 decimal places.

# Input Format

# The next n lines contain the names and marks obtained by a student in five different subjects, each value separated by a space.
# start

# The first line contains an integer n, the number of students.
# The next n lines contains the name and marks obtained by that student.

student_data = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter the name of the student: ")
    marks1 = int(input("Enter the marks of the student in subject 1: "))
    marks2 = int(input("Enter the marks of the student in subject 2: "))
    marks3 = int(input("Enter the marks of the student in subject 3: "))
    marks4 = int(input("Enter the marks of the student in subject 4: "))
    marks5 = int(input("Enter the marks of the student in subject 5: "))
    avg = (marks1 + marks2 + marks3 + marks4 + marks5) / 5
    # key is name and value is avg
    student_data[name] = avg


print(student_data)

# Author: Ansh Garg
# Date: 17-3-23