# Time Complexity is O(Nlog(N)) to O(N^2)[Only if the array is sorted in reverse: very rare case]


def Quick_Sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_value = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot_value:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1

        Quick_Sort(arr, low, pivot_index - 1)
        Quick_Sort(arr, pivot_index + 1, high)


arr = [35, 22, 90, 4, 50, 20, 30, 40, 36]
Quick_Sort(arr)
print(arr)
