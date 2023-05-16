# Stack using function.....
li = []


def push():
    val = int(input("Enetr the number : "))
    li.append(val)
    print(li)


def pop():
    if len(li) == 0:
        print("Stack is empty")
    else:

        # if the pop is assigned a vlaue the removing of the elements will be done from the starting,,,,relation between stack and que [pop()=stack ,,,,pop(0)=queee]
        li.pop(0)
        print(li)


def display():
    for i in range(len(li)):
        print(li[i])


def top():  # it tells the index of the stack,,,,,,
    print(len(li)-1)


choice = 1
while (choice != 4):

    choice = int(input(
        "Enter the choice : Press 1 for adding 2 for deleting 3 for display 4 top of the stack : "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        top()
    elif choice == 5:
        break
