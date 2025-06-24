def Stack():
    arr = []
    choice = int(input("0:Exit 1:Push 2:Pop 3:Peek 4:Traverse 5:Size 6:Is Empty\nEnter choice: "))
    while choice:
        if choice == 1:
            num = int(input("Enter number to push:"))
            arr.append(num)
        elif choice == 2:
            print("Element Popped: ", arr.pop())
        elif choice == 3:
            if len(arr) == 0:
                print("Empty Array")
            else:
                print(arr[-1])
        elif choice == 4:
            if len(arr) == 0:
                print("Empty Array")
            else:
                for i in range(len(arr)-1,-1,-1):
                    print(arr[i])
        elif choice == 5:
            print(len(arr))
        elif choice == 6:
            if len(arr) == 0:
                print("True")
            else:
                print("False")
        else:
            print("Wrong Input")
        choice = int(input("0:Exit 1:Push 2:Pop 3:Peek 4:Traverse 5:Size 6:Is Empty\nEnter choice: "))


Stack()
