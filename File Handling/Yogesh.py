# program to print the data of a file inside the same folder
'''
fl = open("Yogesh Story.txt", "r")
data = fl.read()
print(data)'''

# program for printing the data of a file which is not inside the same folder
'''fl = open(r"C:\Program Files\Google\Chrome\Yogesh Story.txt", "r")
data = fl.read()
print(data)'''


# program to print the upper letter and lower letter
'''fl = open(r"C:\Program Files\Google\Chrome\Yogesh Story.txt", "r")
ucount, lcount = 0, 0
data = " "
while data:
    data = fl.read(1)

    if data.isupper():
        ucount += 1
    else:
        lcount += 1
print(ucount)
print(lcount)'''

# program to print the number of vowels in the sentence.....
'''fl = open(r"C:\Program Files\Google\Chrome\Yogesh Story.txt", "r")
vcount, ccount = 0, 0
data = " "
while data:

    data = fl.read(1)
    if data == ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:

        vcount += 1
    else:
        ccount += 1
print(vcount)
print(ccount)
'''

# program to print the number of words in the text file...
'''fl = open(r"C:\Program Files\Google\Chrome\Yogesh Story.txt", "r")
count = 0
data = " "
while data:

    data = fl.read(1)
    if data == "a":

        count += 1

print(count)'''

# program for printing the data inside the file
'''fl = open("Yogesh Story.txt", "r")
data = fl.readlines()
for i in range(len(data)):
    # This is done because the data itself is in the different lines otherwise it will be printing as the type of list
    print(data[i], end="")'''

# program for finding the word which is used mostly in the txt file
fl = open("Yogesh Story.txt", "r")
data = fl.readlines()
count = 1
for i in range(len(data)):
   