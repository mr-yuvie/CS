# Time Complexity is O(N)
def Linear_Search(arr):
    value = int(input("Enter number to find:"))
    for i in range(len(arr)):
        if arr[i] == value:
            print("Value found at index", i)
            break
    else:
        print("Value not found.")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Linear_Search(arr)
