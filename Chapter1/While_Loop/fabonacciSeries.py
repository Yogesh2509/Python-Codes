num = int(input("Number of elements in series : "))
a = 0
b = 1
print(a, " ", b, end=" ")
for i in range(num-2):
    c = a+b
    a = b
    b = c
    print(c, end=" ")
