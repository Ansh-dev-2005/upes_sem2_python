#print the frequency of each character in the string
a=input("Enter first string: ")
a=a.lower()
a=list(a)
a.sort()
for i in a:
    print(i,a.count(i))
