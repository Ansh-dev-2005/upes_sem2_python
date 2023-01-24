#largest among three numbers without using and
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))
# if a>b :
#     if a>c:
#         print("a is largest")
#     else:
#         print("c is largest")
# else:
#     if b>c:
#         print("b is largest")
#     else:
#         print("c is largest")
# if b>c:
#     if b>a:
#         print("b is largest")
#     else:
#         print("a is largest")
# largest among three number using ternary operator
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
print("a is largest") if a>b and a>c else print("b is largest") if b>c else print("c is largest")