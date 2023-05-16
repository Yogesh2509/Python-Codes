# function for converting dollar into rupee by void and non void form
'''def dol_rupee_nv(d):
    return d*80


def dollar_rupee_v(a):
    print(a*80)


d = int(input("Enter the dollar : "))
print(dol_rupee_nv(d))
dollar_rupee_v(d)'''

# function to print the volume of the cuboid
'''def cuboid(l, b, h):
    return l, b, h


print("Volume of the cuboid is ", cuboid(1, 2, 3))'''

# function to print the cube of the number if given and if not given it will itself print the value of 2

'''
def num(a=2):
    return (a*a*a)


print(num())'''

# function to print true if the both values are same and false if the both values are different


'''def cmp(a, b):
    if (a == b):
        return True
    else:
        return False


a = input("Enter the character : ")
b = input("Enter the character : ")

print(cmp(a, b))'''

# program to print any random number between the two numbers
'''import random
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
print(random.randint(a, b))'''

# program to print if the length of the string are of same lengthz

'''
def str(a, b):
    if len(a) == len(b):
        return True
    else:
        return False


a = input("Enter the string : ")
b = input("Enter the string : ")

print(str(a, b))'''

# function to print a mathemathical expression of x^1/n

'''
def exp(x, n=2):      # always write default value after the  value given by the user
    return x**(1/n)


print(exp(5, 5))'''

# function to print any random number of n digit entered by the user

'''import random
def power(n):
    lr = 10**(n-1)
    ur = 10**n-1
    num = random.randint(lr, ur)
    return num
print(power(3))'''

# function to print


def compare(n1, n2):
    a = n1 % 10
    b = n2 % 10
    if a > b:
        return n2
    else:
        return n1


n1 = int(input("Enter the number : "))
n2 = int(input("Enter the number : "))
print(compare(n1, n2))
