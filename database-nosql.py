#Question 1

import pymongo as p
a = p.MongoClient()
db = a['Students']


#Question 2

r_name = []
r_marks = []
records = {}
l1 = []
for i in range(10):
    name = input('Enter name: ')
    marks = int(input('Enter marks: '))
    r_name.append(name)
    r_marks.append(marks)
for i in range(10):
    records = {'Name':r_name[i],'Marks':r_marks[i]}
    l1.append(records)

#Question 3
col = db['Student_data']
for i in range(10):
    a = l1[i]
    col.insert_one(a)

#Question 4

a = {'Marks':{'$gt':80}}
data = col.find(a)
for i in data:
    print("Name: {} , Marks: {}".format(i['Name'],i['Marks'])
