'''class Student:              #class is a blueprint 
    name = "Singh Shab"             #members of class or instance member
    standard = "12th"
    school = "Udayan Int"


y = Student()                    # Objects
y.name = "Yogesh"
y.standard = "Btech 2nd sem"
y.school = "UIS"

a = Student()
a.name = "Sallu Bhoi"
a.standard = "working"
a.school = "Asain"

print(y.name, y.school, y.standard)
print(type(y))
'''


'''class Student:          # class is a blueprint
    def __init__(self, a, b, c):  # constructor,,,,it is a special type of function which runs itself
        self.name = a  # here a,b,c are always local variable
        self.standard = b
        self.school = c


y = Student("Yogesh", "Btech 1st", "kv")          # Objects
a = Student("Singh shab", "Btech 2nd sem", "kv")
print("His name is", y.name, "study in",
      y.standard, "and he is from", y.school)
print("His name is", a.name, "study in",
      a.standard, "and he is from", a.school)'''


'''class student:
    a = 10  # list method

    def __init__(self):
        self.x = 20            #instance variable
        student.b = 20  # 2nd method

    @staticmethod
    def f1():
        student.c = 3  # 3rd method
        print("HEllo")

    def f2(self):         #instance member function // instance method
        student.d = 40

s1 = student()
s2 = student()
s1.f1()
s2.f2()
student.f1()  # static mehtod can be call through class, object and while instance method can be called only through object'''


class student:
    a = 10  # 1st method

    def __init__(self):
        self.x = 20  # instance variable
        student.b = 20  # 2nd method

    @staticmethod
    def f1(m, n):
        student.c = m  # 3rd method
        print(student.c)

    def f2(self, a):  # instance member function // instance method
        student.d = 40       # 4th method

    @classmethod
    def f3(cls):  # class method
        cls.e = 50  # 5th method
        student.f = 60  # 6th method
        print("Class Method")


student.g = 70  # static variable
s1 = student()
s2 = student()
s1.f1(2, 3)
s2.f2(5)

# static mehtod can be call through class, object and while instance method can be called only through object
student.f1(2, 3)
student.f3()
print(student.__dict__)  # this shows all the methods used in the class
