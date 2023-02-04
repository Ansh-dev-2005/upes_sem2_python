#Write a program in which a user will enter full name .The program should print the first name and first letter of other names in capital letters. and last name me be unlimited with the help of loops




# Path: py15.py

a=input("Enter your full name")
b=a.split()
c=len(b)
i=0
while i<c:

    if i==c-1:
        print(b[i].capitalize(),end=" ")
    else:
        print(b[i][0].title(),end=" ")
    i=i+1
    


