# Time Complexity is O(N^2)


def Selection_Sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        if min_value != i:
            arr[i], arr[min_value] = arr[min_value], arr[i]
    print(arr)


arr = [4, 6, 2, -8, 7, 124, -54, 94, 57, 23, 21, 27]
Selection_Sort(arr)
