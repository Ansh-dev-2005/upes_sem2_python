# list of rollnumber from 1 to 60 and make three group out of it for example group 1 will have 1,4,7 and so on and group 2 will have 2,5,8 and so on and group 3 will have 3,6,9 and so on.
#


# Path: py20.py

# Create list
list1=[]

# Add elements to list
for i in range(1,61):
    list1.append(i)

# Print list
print("List of roll numbers: ",list1)
# divide list into 3 groups of 20 elements each like group 1 is 1,4,7
# group 2 is 2,5,8 and group 3 is 3,6,9'
# Create 3 empty lists
list2=[]
list3=[]
list4=[]
# Add elements to list2
for i in range(0,60,3):
    list2.append(list1[i])
# Add elements to list3
for i in range(1,60,3):
    list3.append(list1[i])
# Add elements to list4
for i in range(2,60,3):
    list4.append(list1[i])
# Print lists
print("Group 1: ",list2)
print("Group 2: ",list3)
print("Group 3: ",list4)
