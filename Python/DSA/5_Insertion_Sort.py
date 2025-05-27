# Time Complexity is O(N^2)
# Loop until you find an element smaller than the sorted part then insert it into sorted part
# First element is always considered sorted and sorted part grows every iteration


def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    print(arr)


arr = [2, 5, 6, 1, 4, 3]
Insertion_Sort(arr)
