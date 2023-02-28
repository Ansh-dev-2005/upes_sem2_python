# Take Input from user two matrix and output multiplication of them without functions


print("Enter the number of rows and columns of first matrix: ")
m=int(input())
n=int(input())
print("Enter the number of rows and columns of second matrix: ")
p=int(input())
q=int(input())
if n!=p:
    print("Matrix multiplication is not possible")
else:
    print("Enter the elements of first matrix: ")
    a=[]
    for i in range(m):
        a.append([])
        for j in range(n):
            a[i].append(int(input()))
    print("Enter the elements of second matrix: ")
    b=[]
    for i in range(p):
        b.append([])
        for j in range(q):
            b[i].append(int(input()))
    result=[]
    for i in range(m):
        result.append([0]*3)
        #for j in range(q):
         #   result[i].append(0)
    print(result)

            
    for i in range(m):
        for j in range(q):
            for k in range(n):
                # print(result[i][j],end=" ")
                result[i][j]+=a[i][k]*b[k][j]
    print("The multiplication of two matrix is: ")
    for r in result:
        print(r)
        



