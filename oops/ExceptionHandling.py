# Solving Runtime Errors ......
'''a = int(input("Enter the no : "))
b = int(input("Enter the no : "))
try:
    print("file open")
    print(a/b)
except Exception as e:
    print("you cannot divide a no by 0 ", e)
finally:
    print("file closed")
'''

a = int(input("Enter the no : "))
b = int(input("Enter the no : "))

try:
    print(a/b)
    c = int(input("Enter the no : "))
    print(c)
    dict = {1: "Yogesh", 2: "Yogi", 3: "Yash"}
    print(dict[4])
    print("20"+10)
    print("file open")
except ZeroDivisionError as z:
    print("you cannot divide a no by 0 ", z)
except ValueError as v:
    print("Please enter valid integer", v)
except TypeError as T:
    print("Invalid operator used")
except NameError:
    print("Please first declare it")
except KeyError:
    print("This key not found")
except Exception as e:
    print("Exception", e)
finally:
    print("file closed")
