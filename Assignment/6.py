# WAP to input a list of scores for N students ina list data type. Find the score of the runner-up and print the output.

a = int(input("Enter number of students: "))
b = []
for i in range(a):
    b.append(int(input("Enter the marks of the student: ")))
b.sort()

print("The runner-up score is", b[-2])

# Author: Ansh Garg
# Date: 17-3-23