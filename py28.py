# Create a dictionary for student data with attributs names ,cgpa, course, sapid dynamicaly
from prettytable import PrettyTable
# import prettytable

student_data = {} 
while 1:
    Roll_no = int(input("Enter Roll No"))
    student = {} 
    name = input("Enter Student Name:")
    student['name']=name
    course = input("Enter Student Course:")
    student['course']=course
    cgpa = float(input("Enter cgpa:"))
    student['cgpa']=cgpa
    mob = int(input("Enter Student Mobile Number:"))
    student['mob']=mob
    student_data[Roll_no]=student
    choice = input("Press Y for continue, N for stop")
    if choice == 'n' or choice == 'N':
        break
    
print(student_data)
max_cgpa = 0.0
topper = 0
for stu in student_data:
    if max_cgpa < student_data[stu]['cgpa']:
        max_cgpa = student_data[stu]['cgpa']
        topper = stu
# Path: py28.py
# print the topper details
print(student_data[topper])
# Make a dictinoary of toppers of each course
# Create a list of courses dynamically

c=list(set([student_data[i]['course'] for i in student_data]))
# for i in student_data:
#     if student_data[i]['course'] not in c:
#         c.append(student_data[i]['course'])

# Create a dictionary of toppers of each course include roll number, name, and CGPA
toppers={}
for i in c:
    toppers[i]={'roll':0,'name':'', 'cgpa':0.0}
for i in student_data:
    if toppers[student_data[i]['course']]['roll'] == 0 or student_data[i]['cgpa']>toppers[student_data[i]['course']]['cgpa']:
        toppers[student_data[i]['course']]['roll']=i
        toppers[student_data[i]['course']]['name']=student_data[i]['name']
        toppers[student_data[i]['course']]['cgpa']=student_data[i]['cgpa']

# Print the toppers of each course
print(toppers)
# print toppers in tabular format
print('Course\tRoll\tName\tCGPA')
for i in toppers:
    print(i,'\t',toppers[i]['roll'],'\t',toppers[i]['name'],'\t',toppers[i]['cgpa'])
