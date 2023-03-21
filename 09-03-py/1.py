# Encrypt the spring input from user and take key as input from user


a=input("Enter the string: ")
b=input("Enter the key: ")
c=""
for i in range(len(a)):
    c+=chr(ord(a[i])+int(b))
print(c)

# Decrypt the string and take key as input from user
a=input("Enter the string: ")
b=input("Enter the key: ")
c=""
for i in range(len(a)):
    c+=chr(ord(a[i])-int(b))
print(c)