# program for finding the number of prime number or composite number in range

range1 = int(input("Enter the number : "))
range2 = int(input("Enter the number : "))
prime = 0
composite = 0

for i in range(range1, range2+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        prime += 1
    else:
        composite += 1
print("No. of prime no. is : ", prime)
print("No. of composite no. is : ", composite)
