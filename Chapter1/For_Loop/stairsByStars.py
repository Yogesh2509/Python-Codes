#program for printing the sTAIRS WITH STARS
num = int(input("Enter the number : "))
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()
