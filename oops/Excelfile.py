'''import csv
obj = open("Student.csv", "w", newline="")
fobj = csv.writer(obj)
fobj.writerow(["Empno", "name", "salary"])
list = []
while True:
    Empno = int(input("Enter the value : "))
    name = input("Enter the name : ")
    salary = float(input("Enter the salary : "))
    list.append([Empno, name, salary])
    ch = int(input("Enter 1 for adding records and 2 for exit : "))
    if ch == 2:
        break
fobj.writerows(list)
'''
import csv
obj = open("Student.csv", "r", newline="")
fobj = csv.reader(obj)
for i in fobj:
    print(i)
