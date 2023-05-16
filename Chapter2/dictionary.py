# dictionary

'''dict = {1: "rahul", 2: "pankaj", 3: "kanishk",
        4: "pranjal", 5: "bhupesh", "a": "anurag", (1, 2, 3): [1, 2, 3], }
dict[2] = "kanchan"
print(dict)
del dict[5]
dict.pop(4)
print(dict)
print(len(dict))
dict.clear()
print(dict)
print(dict.get(5))
print(dict.items())
a = list(dict.items())
print(a[2])
print(dict[7][2])
print(dict.keys())
a = list(dict)
a = list'''


# Taking input from the user to ask name and the marks
dict = {}
for i in range(5):
    name = input("Enter the name : ")
    marks = float(input("Enter the marks : "))
    dict[name] = marks
print(dict)
