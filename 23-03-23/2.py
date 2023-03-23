# Write a program, which will find a list of all numbers between 1000 and 1999 such that each digit at odd place is an even number. Find sum of all odd places digits of every above such number and tell how many unique sum received using a suitable data structure.

# Example:

# one of the possible number is = [1206] sum of odd places' digits = 8


def is_odd_even(num):
    num_str = str(num)
    for i in range(1, len(num_str), 2):
        if int(num_str[i]) % 2 != 0:
            return False
    return True

def get_odd_even_numbers(n):
    count = 0
    num = 1000
    odd_even_numbers = []
    while count < n:
        if is_odd_even(num):
            odd_even_numbers.append(num)
            count += 1
        num += 1
    return odd_even_numbers

def print_numbers(numbers):
    for number in numbers:
        print(number)

n = int(input("Enter the number of odd even numbers to find: "))
odd_even_numbers = get_odd_even_numbers(n) 
print_numbers(odd_even_numbers)

