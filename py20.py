# Removing all duplicacy from string
a=input("Enter first string: ")
# Convert string into capital letters
a=a.upper()
b=list(a)
c=[]
for i in b:
    if i not in c:
        c.append(i)
print("".join(c))
