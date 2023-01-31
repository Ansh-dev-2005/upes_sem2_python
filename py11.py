#Take input from user and print all numbers till that number and square and cube of that number format() which should we aligned properly
a=int(input("enter the number"))
print("{0:<10s} {1:<10} {2:<10s}".format("number","square","cube"))
for i in range(1,a+1):
    print("{0:<10d} {1:<10d} {2:<10d}".format(i,i**2,i**3))
