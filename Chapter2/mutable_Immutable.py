'''a=5
print(a)
print(id(a))
a=10
print(id(a))'''


# question to print the biggest word in a string
'''a = input("Enter the string : ")
word = a.split(" ")
max = word[0]
for i in range(len(word)):
    if len(word[i]) > len(max):
        max = word[i]
length = len(max)
for i in range(len(word)):
    if len(word[i]) == length:

        print(word[i])'''

# write a program that create a list of All the intezers upto 100 that are multiple of 3 and 5
num = 100
li = []
for i in range(1, num+1):
    if i % 3 == 0 or i % 5 == 0:
        li.append(i)
print(li)
