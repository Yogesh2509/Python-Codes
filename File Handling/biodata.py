import csv

fl = open("excel.csv", "w", newline="")
fh = csv.writer(fl)
fh.writerow(["Name", "Marks", "Rollno"])
for i in range(5):
    print("Student record : ")
    rollno = int(input("Enter the no : "))
    name = input("Enter the name : ")
    marks = float(input("Enter the marks : "))
    sturec = [rollno, name, marks]
    fh.writerow(sturec)
