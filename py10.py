#Take input from user and print all numbers till that number and square and cube of that number using % operator which should we aligned properly
a=int(input("enter the number"))
print("number","square","cube")
for i in range(1,a+1):
    print("%-10d %-10d %-10d"%(i,i**2,i**3))