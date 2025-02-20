# Given two crystal balls that will break if dropped
# from high enough distance, determine the exact spot
# in which it will break in the most optimized way
# For eg. Array would look like = [0,0,0,0,1...]
# where 0 means the ball doesn't break and 1 means ball breaks
# Time complexity is O(sqrt(N)) cause we jump sqrt(N) times and then linearly check between the last jump to the point where it breaks

import math


def Crystal_Ball_Problem(arr):

    jump_amount = math.floor(math.sqrt(len(arr)))
    for i in range(0, len(arr), jump_amount):
        if arr[i]:
            break
    i -= jump_amount

    for j in range(i, i + jump_amount):
        if arr[j]:
            print("The index where it breaks first is:", j)
            break
    else:
        print("The Ball never breaks.")


arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Crystal_Ball_Problem(arr)
