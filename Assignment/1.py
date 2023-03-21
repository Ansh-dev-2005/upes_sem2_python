# Convert uppercase string to lowercase without using inbuilt function lower.
# add Author name and date in all the files

def lower(s):
    s1 = ""
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            s1 += chr(ord(i) + 32)
        else:
            s1 += i
    return s1

s = input("Enter a string: ")
print(lower(s))

# Author: Ansh Garg
# Date: 17-3-23