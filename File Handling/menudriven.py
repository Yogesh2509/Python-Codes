# menudriven program
'''li = []


def insertion():
    if len(li)>=10:
        print("Stack is empty")
    val = int(input("Enetr the number : "))
    li.append(val)
    print(li)


def delete():
    li.remove()
    print(li)


def sorting():
    li.sort()
    print(li)


def trav():
    for i in range(len(li)):
        print(li[i])


def search():
    val = input("Enter the element : ")
    if val in li:
        print("Element Found")
    else:
        print("Element not Found")


choice = 1
while (choice != 4):

    choice = int(input(
        "Enter the choice :Press 1 for Inserting 2 for deleting 3 for sorting 4 for traversing 5 for searching and 6 for exiting : "))
    if choice == 1:
        insertion()
    elif choice == 2:
        delete()
    elif choice == 3:
        sorting()
    elif choice == 4:
        trav()
    elif choice == 5:
        search()
    elif choice == 6:
        break
'''

'''
HighestPr = []
NormalPr = []
LowestPr = []
while True:
    print()
    print("Enter your choice as per given -")
    print("1 = For insert element Enter insert ")
    print("2 = Search for Element  enter search ")
    print("3 = for change Priority enter change")
    print("4 = For Exit  enter exit ")
    print()
    user = input("Enter your choice :- ")
    if user == "insert":
        data = input("Enter element :- ")
        priority = input(
            "Enter  Priority(Highest/ Normal / Lowest (H/N/L):  :- ")
        if priority == "H":
            HighestPr.append(data)
        elif priority == "N":
            NormalPr.append(data)
        elif priority == "L":
            LowestPr.append(data)
    elif user == "search":
        data = input("Enter element :- ")
        if data in HighestPr:
            print(data, "Present in HighestPr Queue")
        elif data in NormalPr:
            print(data, "Present in NormalPr Queue")
        elif data in LowestPr:
            print(data, "Present in LowestPr Queue")
        else:
            print("Not found !!!!")
    elif user == "change":
        data = input("Enter element :- ")
        newpri = input(" Want to Increase/Decrease its priority (I/D) ? ")
        if data in HighestPr:
            HighestPr.remove(data)
            if newpri == "D":
                NormalPr.append(data)

        elif data in NormalPr:
            NormalPr.remove(data)
            if newpri == "D":
                LowestPr.append(data)
            else:
                HighestPr.append(data)

        elif data in LowestPr:
            LowestPr.remove(data)
            if newpri == "I":
                NormalPr.append(data)
        else:
            print("Not found !!!!")

    else:
    	print("HighestPr Queue :-", HighestPr)
        print("NormalPr Queue :-", NormalPr)
        print("LowestPr Queue :-", LowestPr)
        break
'''

low = []
mid = []
high = []


def insertion():
    value = input("Enter the value : ")
    priority = input("Entert the priority : press low mid or high : ")
    if priority == "low":
        low.append(value)
    elif priority == "mid":
        mid.append(value)
    elif priority == "high":
        high.append(value)


def search():
    value = input("Enter the element : ")
    if value in high:
        print("Element is in highest priority")
    elif value in low:
        print("Element is in lowest priority")
    elif value in mid:
        print("Element is in mid priority")


def change():
    value = input("Enter the element : ")
    newpriority = input(
        "Press I for increasing priority or \npress D for decreasing the priority ")
    if value in low:
        if newpriority == "I":
            low.remove(value)
            mid.append(value)
        elif newpriority == "D":
            print("It is in lowest priority")
        if value in mid:
            if newpriority == "I":
                mid.remove(value)
                high.append(value)
            elif newpriority == "D":
                mid.remove(value)
                low.append(value)
        if value in high:
            if newpriority == "I":
                print("It is in highest priority")
            elif newpriority == "D":
                high.remove(value)
                mid.append(value)


choice = 1
while choice != 4:
    choice = int(
        input("Enter the choice :\n1- Insertion\n2- Search\n3- Change priority \n"))
    if choice == 1:
        insertion()
    elif choice == 2:
        search()
    elif choice == 3:
        change()
    else:
        print("Enter the valid choice")
        break
