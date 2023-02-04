#Take input from user and check if it is a palindrome or not


word = input("Enter a word: ")
if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

