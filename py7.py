#print prime number using while loop in given range
a=int(input("enter the starting number"))
b=int(input("enter the ending number"))
i=a
while i<=b:
    j=2
    while j<i:
        if i%j==0:
            break
        j=j+1
    else:
        print(i, end=" ")
    i=i+1


