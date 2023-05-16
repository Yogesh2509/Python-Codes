# program for counting positive and negative number

num = input("Enter a number: ")
even_pos_count = 0
odd_pos_count = 0

for i in range(len(num)):
    if i % 2 == 0:
        if int(num[i]) % 2 == 0:
            even_pos_count += 1
        else:
            odd_pos_count += 1
    else:
        if int(num[i]) % 2 == 0:
            odd_pos_count += 1
        else:
            even_pos_count += 1

print("Total even positions:", even_pos_count)
print("Total odd positions:", odd_pos_count)
