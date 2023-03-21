# Create a dictionary for student data with attributs names ,cgpa, course, sapid


student_data = {} # creating an empty dictionary for storing final data

while 1:

  Roll_no = int(input("Enter Roll No"))

  #collect information about individual student

  student = {} # a dictionary for representing individual student

  name = input("Enter Student Name:")

  student['name']=name

  course = input("Enter Student Course:")

  student['course']=course

  cgpa = float(input("Enter cgpa:"))

  student['cgpa']=cgpa

  mob = int(input("Enter Student Mobile Number:"))

  student['mob']=mob

   

  # add student to nested dictionary

  student_data[Roll_no]=student

   

  #take choice for next entry

  choice = input("Press Y for continue, N for stop")

  if choice == 'n' or choice == 'N':

    break

     

# find the topper of the class

max_cgpa = 0.0

topper = 0

for stu in student_data:

  if max_cgpa < student_data[stu]['cgpa']:

    max_cgpa = student_data[stu]['cgpa']

    topper = stu



print("Following is student has secured maximum cgpa:")

print(f"Student Roll No: {topper}")

print(f"Student Name: {student_data[topper]['name']}")

print(f"Student Course: {student_data[topper]['course']}")

print(f"Student CGPA: {student_data[topper]['cgpa']}")

print(f"Student Mobile Number: {student_data[topper]['mob']}")


