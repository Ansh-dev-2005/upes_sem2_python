# Write a Python program to count the most and least common characters in a given string.


string = input("Enter a string: ")
d = {}
for i in string:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# print most common character
max = 0
for i in d:
    if d[i] > max:
        max = d[i]
        max_char = i
print("Most common character is", max_char, "with count", max)

# print least common character
min = 100000000
for i in d:
    if d[i] < min:
        min = d[i]
        min_char = i
print("Least common character is", min_char, "with count", min)

# Author: Ansh Garg
# Date: 17-3-23
