# function to count the number of digits in a number

def no_of_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# function to print this pattern like input is 25 it should print 2^2 + 5^2 power should be number of digits in the number for example 230 it should print 2^3 + 3^3 + 0^3
def power_sum(n):
    s = 0
    while n > 0:
        r = n % 10
        s += r ** no_of_digits(n)
        n //= 10
    return s


n=int(input("Enter a number:"))
print(no_of_digits(n))
print(power_sum(n))
