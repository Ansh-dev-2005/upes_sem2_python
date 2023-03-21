# Write a python script that receives a collection of fruits with their quantity (in kg) & purchasing price per unit(kg). Use suitable data structure to store the information so that following queries can be handled easily. Also, print the answer of each query.

# Total quantity of fruits collected.
# Total cost of fruits collected.
# Total cost of each fruit.
# Cheapest fruit in collection
# Most costly fruit and its quantity in the collection.

fruits = {}
n = int(input("Enter number of fruits: "))
for i in range(n):
    fruit = input("Enter the name of the fruit: ")
    quantity = int(input("Enter the quantity of the fruit: "))
    price = int(input("Enter the price of the fruit: "))
    fruits[fruit] = [quantity, price]

print("Total quantity of fruits collected:", sum([fruits[fruit][0] for fruit in fruits]))
print("Total cost of fruits collected:", sum([fruits[fruit][0] * fruits[fruit][1] for fruit in fruits]))
print("Total cost of each fruit:")
for fruit in fruits:
    print(fruit, ":", fruits[fruit][0] * fruits[fruit][1])
print("Cheapest fruit in collection:", min(fruits, key=lambda fruit: fruits[fruit][1]))
print("Most costly fruit and its quantity in the collection:", max(fruits, key=lambda fruit: fruits[fruit][1]), fruits[max(fruits, key=lambda fruit: fruits[fruit][1])][0])

# Author: Ansh Garg
# Date: 17-3-23