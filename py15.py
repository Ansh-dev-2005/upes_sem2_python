#Write a program to check whether the two strings are anagram or not and there should not any limit on the length of the string by sorting method
a=input("Enter first string: ")
b=input("Enter second string: ")
#make both sting upper case
a=a.upper()
b=b.upper()
#sort the string
a=sorted(a)
b=sorted(b)
#check if sorted string are equal
if a==b:
    print("Anagram")
else:
    print("Not an anagram")

if len(a) != len(b):
    print("Not an anagram")
#parameters of sorted method
#sorted(iterable, key=None, reverse=False)
