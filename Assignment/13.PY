# Write a program to receive an integer and find its binary equivalent. (i) (Hint: To obtain octal equivalent of an integer, divide it continuously by 2 till dividend doesn’t become zero, then write the remainders obtained in reverse direction.)


a = int(input("Enter a number: "))
b = ""
while a > 0:
    b += str(a % 2)
    a //= 2
print(b[::-1])

# Author: Ansh Garg
# Date: 17-3-23