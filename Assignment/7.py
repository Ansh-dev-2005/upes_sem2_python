# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of country stamps. Find the total number of distinct country stamps using a suitable data type.


n = int(input("Enter number of stamps: "))
stamps = set()
for i in range(n):
    country = input("Enter the name of the country for stamp {}: ".format(i+1))
    stamps.add(country)

print("Total distinct country stamps:", len(stamps))

# Author: Ansh Garg
# Date: 17-3-23
