#sum of series 1/1!+1/2!+1/3!+1/4!+1/5!+1/6!+1/7!+1/8!+1/9! to n terms
a=int(input("Enter the number of terms"))
i=1
sum=0
while i<=a:
    j=1
    fact=1
    while j<=i:
        fact=fact*j
        j=j+1
    sum=sum+(1/fact)
    i=i+1
print(sum)
    