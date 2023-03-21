# create dictionary set keys and values
s1={'name':'XYZ','course':'BTECH','cgpa':8.5,'salary':750000}
s2={'name':'ABC','course':'MTECH','cgpa':9.0,'salary':800000}


# create a list of dictionaries
s=[s1,s2]

# print the list
print(s[0])
# Print the cgpa of student 1
print(s[0]['cgpa'])

s3={1:100,2:200,3:300,4:400,5:500}
# Update the value of key 3 to 350
s3[3]=350
# Print the dictionary
print(s3)
# list of students with highest pays course wise
# create a list of dictionaries
s=[s1,s2]
# create a list of courses
c=['BTECH','MTECH']
# create a list of highest pays
h=[0,0]
# create a list of highest pays students
hs=['','']
# iterate over the list of students
for i in s:
    # iterate over the list of courses
    for j in range(len(c)):
        # check if the course of student is equal to course in list of courses
        if i['course']==c[j]:
            # check if the salary of student is greater than highest pay of course
            if i['salary']>h[j]:
                # update the highest pay of course
                h[j]=i['salary']
                # update the highest pay student of course
                hs[j]=i['name']
# print the highest pay students
print(hs)
