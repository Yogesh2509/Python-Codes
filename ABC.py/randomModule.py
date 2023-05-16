import random
'''print(random.random())
print(random.randint(10, 20))  # it prints any random integer value
print(random.uniform(10, 20))  # it prints any random float value
# it prints any random value from 0 to the given number
print(random.randrange(10))
# to print any random number between 10 and 20 and it will be coming in a gap of 2,,
# the first number may appear sometime but the last number may not appear at the same time
print(random.randrange(10, 20, 2))
'''

# In a school of 100 students 3 students are selected at random to present a bokey to the guests


def event():
    stu1 = random.randint(1, 100)
    stu2 = random.randint(1, 100)
    stu3 = random.randint(1, 100)
    if (stu1 == stu2 or stu2 == stu3 or stu3 == stu1):
        event()
    else:
        print(stu1, stu2, stu3)


event()
