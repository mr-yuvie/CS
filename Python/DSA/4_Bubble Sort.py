# Time Complexity is O(N^2)
# Swap positions if the next number is smaller than the previous one [x < x + 1]
# Last element is always sorted so reduce the loop by 1 every single iteration

def Bubble_Sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


arr = [190, -1, 12, 42, 42, 1, -1, 872, -21]
Bubble_Sort(arr)
