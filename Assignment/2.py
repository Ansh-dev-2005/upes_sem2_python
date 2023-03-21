#  Find the sum of rows and columns of matrix of given order (row x column)
# take user input for row and column

row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
matrix = []
for i in range(row):
    matrix.append([])
    for j in range(column):
        matrix[i].append(int(input("Enter element: ")))


for i in range(row):
    sum = 0
    for j in range(column):
        sum += matrix[i][j]
    print("Sum of row", i+1, "is", sum)

for i in range(column):
    sum = 0
    for j in range(row):
        sum += matrix[j][i]
    print("Sum of column", i+1, "is", sum)

# Author: Ansh Garg
# Date: 17-3-23