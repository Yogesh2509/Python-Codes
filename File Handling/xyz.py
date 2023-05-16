# program to write the new data in a pre file,,,,,,,,a new file will be created
'''fl = open("Yogesh Story.txt", "w")       #here w refers to write mode
num = int(input("Enter the number of students : "))
for i in range(num):
    name = input("Enter the name : ")
    fl.write(name+"\n") '''       # it concatinates the lines......


# program to write the new data in a pre file,,,,,in append mode the file will be edited to the next
'''fl = open("Yogesh Story.txt", "a")        #here a refers to append mode
num = int(input("Enter the number of students : "))
for i in range(num):
    name = input("Enter the name : ")
    fl.write(name+"\n") '''   # it concatinates the lines......


#program to print the appended data in a proper table......
'''fl = open("Yogesh Story.txt", "a")  # here a refers to append mode
record = []
num = int(input("Enter the number of students : "))
for i in range(num):
    name = input("Enter the name : ")
    Rno = int(input("Enter the Rno : "))
    marks = float(input("Enter the marks : "))
    r = name+" "+str(Rno)+" "+str(marks)+"\n"
    record.append(r)
    fl.writelines(record)'''

#
fl = open("Yogesh Story.txt", "w+")  # here a refers to append mode
record = []
num = int(input("Enter the number of students : "))
for i in range(num):
    name = input("Enter the name : ")
    Rno = int(input("Enter the Rno : "))
    marks = float(input("Enter the marks : "))
    r = name+" "+str(Rno)+" "+str(marks)+"\n"
    record.append(r)
    fl.writelines(record)
data = fl.readline()
print(data)
