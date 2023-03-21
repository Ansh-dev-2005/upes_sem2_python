# menu driven program for permutation and combination

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
def permutation(n,r):
    return fact(n)/fact(n-r)
def combination(n,r):
    return fact(n)/(fact(r)*fact(n-r))
print ("1. Permutation")
print ("2. Combination")
print ("3. Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter n: "))
        r = int(input("Enter r: "))
        print ("Permutation is",permutation(n,r))
    elif choice == 2:
        n = int(input("Enter n: "))
        r = int(input("Enter r: "))
        print ("Combination is",combination(n,r))
    elif choice == 3:
        break
    else:
        print ("Invalid choice")