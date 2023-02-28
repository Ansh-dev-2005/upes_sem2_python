# Ask user the number till the user wants to continue and print positive and negative numbers and zeros
p = 0
n1 = 0
z = 0
while True:
    n = input("Enter the number: ")
    if n.isdigit() or (n[0] == '-' and n[1:].isdigit()):
        n = int(n)
        if n > 0:
            p += 1
        elif n < 0:
            n1 += 1
        else:
            z += 1
    else:
        print("Input is not an integer.")

    ch = input("Do you want to continue (y/n): ")
    ch = ch.lower()
    if ch == 'n':
        break
    elif ch == 'y':
        continue
    else:
        print("Invalid choice")
        break

print("Number of positive numbers: ", p)
print("Number of negative numbers: ", n1)
print("Number of zeros: ", z)
# print using f string
print(f"Number of positive numbers: {p}")
print(f"Number of negative numbers: {n1}")
print(f"Number of zeros: {z}")
