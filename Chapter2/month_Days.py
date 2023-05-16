# dictonary telling the days in months

dict = {"jan": 31, "feb": 28, "march": 31, "april": 30, "may": 31, "june": 30,
        "july": 31, "aug": 31, "sep": 30, "oct": 31, "nov": 30, "dec": 31}
month = input("Enter the month : ")
print(dict[month])
a = list(dict.keys())  # printing all the months in asscending order
a.sort()
print(a)

for i in dict:
    if dict[i] == 31:  # print all the months with 31 days
        print(i)
for i in dict:
    if dict[i] == 30:  # print all the months with 30 days
        print(i)
