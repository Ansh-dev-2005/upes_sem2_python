#reverse every word of the statement and print it for example My name is ansh and output should be yM eman si hsnA 
a=input("Enter first string: ")
a=a.split()
for i in a:
    i=list(i)
    i.reverse()
    print("".join(i),end=" ")
    


