'''str = "Devank"
list = list(str)  # it converts string to a list
print(list)

# to input a list from a user we use the eval
list = eval(input("Enter the number : "))
print("Your list is ", list)'''

# the data which we does not want to change the datatype
tuple = (2, 5, 15, 25, 36)
list = [2, 5, 15, 25, 36]
list[2] = 20
print(list)

tuple = 20
print(tuple)  # tuple does not support any item assignment
