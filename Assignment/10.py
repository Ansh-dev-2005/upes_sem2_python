# Create a list that contains the names of 5 students of your class. a) Ask the user to input one name and add it to the list. b) sort the list elements in ascending order without any predefined or in-build functions.

def sort_list(student_list):
    for i in range(len(student_list)):
        for j in range(i+1, len(student_list)):
            if student_list[i] > student_list[j]:
                student_list[i], student_list[j] = student_list[j], student_list[i]


student_list = []

for i in range(5):
    student_list.append(input("Enter the name of the student: "))

name = input("Enter the name of the student to be added: ")
student_list.append(name)

sort_list(student_list)

print("The sorted list is:", student_list)

# Author: Ansh Garg
# Date: 17-3-23