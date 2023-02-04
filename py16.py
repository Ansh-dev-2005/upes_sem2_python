#First sort the string and then reverse it and then print it

a=input("Enter first string: ")
#sort the string
a=sorted(a)
#reverse the string
a.reverse()
#print the string in string format
print("".join(a))