list = [2, 5, 7, 8, 15]
print(len(list))
# del list[2]
print(list)
# to delete the numbers starting from 2nd to the number between the 4th number
'''del list[2:4]
print(list)'''
print(list.index(5))  # to determine the position of the given number
list.append(20)  # to add a single item to the datatype
print(list)
list.insert(3, 9)  # to add a sinlge item to any specific position
print(list)
list2 = [25, 30, 40]
# to add the numbers of a new datatype to the older datatype
list.extend(list2)
print(list)
list.append(list2)  # to add the whole new datatype to the older datatype
print(list)
