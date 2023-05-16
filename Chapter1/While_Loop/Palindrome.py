num = int(input("Enter the number : "))
n = num
rev = 0
while (num != 0):
    r = num % 10
    rev = rev * 10 + r
    num = num // 10
if n == rev:
    print("Number is Palindrome")
else:
    print("Number is not a Palindrome")
