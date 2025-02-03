# You can define your own array but it should be sorted for the binary search to be implemented.
# Time Complexity is O(log(N))


def Binary_Search(L):
    value = int(input("Enter number to find:"))
    steps = 0
    MIN = 0
    MAX = len(L) - 1
    while MIN < MAX:
        mid = (MIN + MAX) // 2
        if value == L[mid]:
            steps += 1
            print("Value found at index:", mid)
            break
        elif value > L[mid]:
            MIN = mid + 1
            steps += 1
        elif value < L[mid]:
            MAX = mid - 1
            steps += 1
    else:
        print("Number not found in the array:", value)

    print("Total steps:", steps)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Binary_Search(L)
