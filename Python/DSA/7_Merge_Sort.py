# Time Complexity is O(Nlog(N))


def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l_half = arr[:mid]
    r_half = arr[mid:]

    Merge_Sort(l_half)
    Merge_Sort(r_half)

    i = j = k = 0

    while i < len(l_half) or j < len(r_half):
        if i < len(l_half) and (j >= len(r_half) or l_half[i] < r_half[j]):
            arr[k] = l_half[i]
            i += 1
        else:
            arr[k] = r_half[j]
            j += 1
        k += 1

    # while i < len(l_half) and j < len(r_half):
    #     if l_half[i] < r_half[j]:
    #         arr[k] = l_half[i]
    #         i += 1
    #     else:
    #         arr[k] = r_half[j]
    #         j += 1
    #     k += 1

    # while i < len(l_half):
    #     arr[k] = l_half[i]
    #     i += 1
    #     k += 1

    # while j < len(r_half):
    #     arr[k] = r_half[j]
    #     j += 1
    #     k += 1


arr = [35, 22, 90, 4, 50, 20, 30, 40, 1]
Merge_Sort(arr)
print(arr)
