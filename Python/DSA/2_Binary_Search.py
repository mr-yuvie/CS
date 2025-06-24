# You can define your own array but it should be sorted for the binary search to be implemented.
# Time Complexity is O(log(N))


def Binary_Search(L, target):
    MIN = 0
    MAX = len(L) - 1
    while MIN <= MAX:
        mid = (MIN + MAX) // 2
        if target > L[mid]:
            MIN = mid + 1
        elif target < L[mid]:
            MAX = mid - 1
        else:
            return mid
    return -1  # Not Found


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Binary_Search(L, 1))
