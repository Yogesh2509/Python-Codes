# program to print armstrong number

num = int(input("Enter the number : "))
n = num
arm = 0
while (num != 0):
    r = num % 10
    arm = arm+r*r*r
    num = num//10
if n == arm:
    print("Number is Armstrong")
else:
    print("Number is not a Armstrong")
