#print the frequency of each character in the string check for duplicacy
#
a=input("Enter first string: ")
# Convert string into capital letters
a=a.upper()
b=list(a)
c=[]

for i in b:
    if i not in c:
        c.append(i)
for i in c:
    print(i,"=",b.count(i))
#
#


