# use data prepared in 14.py
#and create another data that stores selling price of each fruit per unit with a profit of 10% if the quantity is more than 10kg, 20% in case quantity is less than 10 kg.


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

selling_price = {}
for fruit in fruits:
    if fruits[fruit][0] > 10:
        selling_price[fruit] = fruits[fruit][1] * 1.1
    else:
        selling_price[fruit] = fruits[fruit][1] * 1.2

print("Selling price of each fruit:")
for fruit in selling_price:
    print(fruit, ":", selling_price[fruit])

# Author: Ansh Garg
# Date: 17-3-23