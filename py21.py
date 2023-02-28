# modifying element in a list
#
# # Path: py21.py

list=[1,2,3,4,5,6,7,8,9,10]
print("id of list: ",id(list))
print("List before modification: ",list)
# Modify element at index 0 
list[0]=100
# Modify element at index 5
list[5]=200
# Modify element at index 9
list[9]=300
print("List after modification: ",list)
# print id
print("id of list: ",id(list))
# insertion of element in a list
# append() method
list.append(400)
print("List after appending: ",list)
# insert() method
list.insert(0,500)
print("List after inserting: ",list)
#slice operator
list[0:4]=[600]
print("List after inserting: ",list)
# extend() method
list.extend([700,800,900])
print("List after extending: ",list)
# list.append([1000,1100,1200])
# print("List after appending: ",list)
# deletion of element in a list
# pop() method
list.pop()
print("List after popping: ",list)


