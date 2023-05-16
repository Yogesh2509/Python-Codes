# Program to print fabonacci series
a = 0
b = 1
li = []
li.append(a)
li.append(b)
n = int(input("Enter the number of elements in series : "))

for i in range(n-2):
    c = a+b
    a = b
    b = c
    li.append(c)
print(li)
