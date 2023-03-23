# A person went to the market for grocery items. He picked items from a super store and stand in a line for billing. The billing counter has a hanging notice that the person stands first in line will get billing service first, whereas a person stands at last will get service in last. No one in middle of the line is allowed until all his/her front get serviced. Write a python code to implement the scenario using two separate functions for in and out. Find the length of line for each person in and out to/from the line.

def in_line():
    global line
    line.append(1)
    print("You are in line")
    print("Length of line is",len(line))

def out_line():
    global line
    line.pop(0)
    print("You are out of line")
    print("Length of line is",len(line))

line = []
while True:
    print("1. In line")
    print("2. Out line")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        in_line()
    elif choice == 2:
        out_line()
    elif choice == 3:
        break
    else:
        print("Invalid choice")