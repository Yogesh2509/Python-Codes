# program for finding the number is prime or composite in range

range1 = int(input("Enter the number : "))
range2 = int(input("Enter the number : "))
for i in range(range1, range2+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, "Number is prime")
    else:
        print(i, "Number is composite")
