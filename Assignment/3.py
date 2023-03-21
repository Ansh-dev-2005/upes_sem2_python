# Find the total number of alphabets, digits orspecial characters in a string.

a=input("Enter a string:")
count1=0
count2=0
count3=0
for i in a:
    if i.isalpha():
        count1+=1
    elif i.isdigit():
        count2+=1
    else:
        count3+=1
print("Alphabets:",count1)
print("Digits:",count2)
print("Special characters:",count3)

# Author: Ansh Garg
# Date: 17-3-23
