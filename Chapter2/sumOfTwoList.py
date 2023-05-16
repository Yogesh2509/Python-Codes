# program to print sum of two list in another list
a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
c = []
for i in range(len(a)):
    value = a[i]+b[i]
    c.append(value)
print(c)
