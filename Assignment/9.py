def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates

# prompt the user to input a list of numbers
input_string = input("Enter a list of numbers separated by spaces: ")
my_list = [int(n) for n in input_string.split()]

# find duplicates in the list
duplicates = find_duplicates(my_list)

# print the results
if duplicates:
    print("The following values appear more than once in the list:")
    print(duplicates)
else:
    print("There are no duplicate values in the list.")


# Author: Ansh Garg
# Date: 17-3-23
