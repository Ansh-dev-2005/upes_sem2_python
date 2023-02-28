# Print minimum and maximum values of a list entered by user without using inbuild function
# # take list from user
l=[]
n=int(input("Enter the number of elements in list: "))
for i in range(0,n):
    ele=int(input())
    l.append(ele)
print(l)

min=l[0]
max=l[0]
for i in l:
    if i<min:
        min=i
    if i>max:
        max=i
print("Minimum value in list is: ",min)

print("Maximum value in list is: ",max)
