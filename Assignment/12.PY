# Write a program to print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.

for i in range(24):
    if i == 0:
        print("12 Midnight")
    elif i < 12:
        print(f"{i} AM")
    elif i == 12:
        print("12 Noon")
    else:
        print(f"{i-12} PM")

# Author: Ansh Garg
# Date: 17-3-23