# Time Complexity is O(N^2)


def Bubble_Sort(arr):
    for i in range(1, len(arr) + 1):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


arr = [190, -1, 12, 42, 42, 1, -1, 872, -21]
Bubble_Sort(arr)
