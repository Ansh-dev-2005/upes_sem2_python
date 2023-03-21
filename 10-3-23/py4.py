def is_armstrong(num):
    """Check if a number is an Armstrong number."""
    # Convert the number to a string to calculate the length
    num_str = str(num)
    n = len(num_str)

    # Calculate the sum of the digits raised to the nth power
    digit_sum = sum(int(digit)**n for digit in num_str)

    # Check if the sum is equal to the original number
    return digit_sum == num


def get_armstrong_numbers(n):
    """Generate the first n Armstrong numbers."""
    count = 0
    num = 0
    armstrong_numbers = []
    while count < n:
        if is_armstrong(num) and num != 0:
            armstrong_numbers.append(num)
            count += 1
        num += 1
    return armstrong_numbers


def print_numbers(numbers):
    """Print a list of numbers."""
    for number in numbers:
        print(number)


# Prompt the user for input
n = int(input("Enter the number of Armstrong numbers to find: "))

# Get the first n Armstrong numbers
armstrong_numbers = get_armstrong_numbers(n)

# Print the Armstrong numbers
print_numbers(armstrong_numbers)
