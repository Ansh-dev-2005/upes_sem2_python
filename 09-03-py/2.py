# Print the pyramid of starts take input from user consider every star as an element

# a=int(input("Enter the number of rows: "))
# for i in range(a):
#     for j in range(i+1):
#         print("*",end=" ")

# print()

a=int(input("Enter the number of rows: "))
for i in range(a):
    print(" "*(a-i),end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

