'''import math

#methods to print the same number which is nearest intezer value

a = 3.25
print(math.floor(3.25))
print(round(3.25))
print(int(3.25))
'''
'''str = "hello"
str1 = "world"
# join
a = "$".join(str)
print(a)
s = "i am doing python programming"
l = s.split("a")
print(l)
p = s.replace("python", "java")
print(p)'''

# to encrypt a string letter by letter then decrypt the encrypted string


def encrypt(strr, enkey):
    return enkey.join(strr)  # here enkey is joined in each alphabet of sttr


def decrpt(strr, enkey):
    return strr.split(enkey)  # here split removes the enkey from the sttr


mainstr = input("Enter the main string : ")
encryptstr = input("Enter the Encrypted string : ")
enstr = encrypt(mainstr, encryptstr)
deLst = decrpt(mainstr, encryptstr)
destr = "".join(deLst)  # we put "" because to convert deLest into string
print(enstr)
print(destr)
