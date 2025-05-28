# Time Complexity is O(N^2)


def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    print(arr)


arr = [2, 5, 6, 1, 4, 3]
Insertion_Sort(arr)
