# factorial of a number by function
def fact(n):
    fact = 1
    while (n != 1):
        fact = fact*n
        n -= 1
    print(fact)


n = int(input("Enter the number : "))
fact(n)
