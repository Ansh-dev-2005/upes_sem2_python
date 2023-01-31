#Take input from user and print all numbers till that number and square and cube of that number using f string method which should we aligned properly

a=int(input("enter the number"))
print(f"{'number':<10} {'square':<10} {'cube':<10}")
for i in range(1,a+1):
    print(f"{i:<10} {i**2:<10} {i**3:<10}")