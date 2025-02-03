import numpy as np
from numpy import random

# # FIRST CLASS

# a = np.array([1, 2, 3])
# b = np.array([[6.0, 7.5, 8.0], [9.0, 10.0, 11.0]])

# # Get Dimension
# print(a.ndim)
# print(b.ndim)

# # Get Shape
# print(a.shape)
# print(b.shape)

# # Get Data Type of array
# print(type(a))

# # Changing Data Type
# a = np.array([1, 2, 3],np.float32)
# b = np.array([[6.0, 7.6, 8.0], [9.0, 10.0, 11.0]],np.int32)

# # Get Type of Data
# print(a, a.dtype)
# print(b, b.dtype)

# # Get Number of Elements
# print(a.size)
# print(b.size)

# a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a)

# # Get a Specific Element [r,c]
# print(a[1,5])

# # Get a Specific Row [r]
# print(a[0])

# # Get a Specific Column [:, c]
# print(a[:, 1])

# # Get a group of elements [r,startindex:endindex:stepsize]
# print(a[0, 1:6:2])

# # To change an element in a row i.e. arrays are mutable
# a[1,-2] = 20
# print(a)

# # To change an element in all columns
# a[:, 2] = [1, 2]

# # 3-D example
# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(b)

# # Get a specific element here (work outside in)
# # To get 4
# print(b[0,1,1])

# # To change an element
# # Replacing 5 with 7
# b[1,0,0] = 7
# print(b)


# # SECOND CLASS

# a = np.array([[-3, 8], [7, 5]])
# b = np.array([[4, 5], [9, 10]])
# c = np.array([[[4, 5], [6, 7]], [[8, 9], [10, 11]]])
# d = np.array(
#     [
#         [[[4, 5], [6, 7]], [[8, 9], [10, 11]]],
#         [[[12, 13], [14, 15]], [[16, 17], [18, 19]]],
#     ]
# )
# e = np.array([[1.278, 2.345], [3.954, 4.784]])

# # Math Functions --> Both numbers and arrays are viable arguments. (a,b,c): c is the return array type.
# # Addition``
# print(np.add(a, b))

# # Subtraction
# print(np.subtract(a, b))

# # Multiplication
# print(np.multiply(a, b))

# # Division
# print(np.divide(a, b))

# # Remainder
# print(np.mod(a, b))

# # Quotient & Remainder
# print(np.divmod(a, b))

# # Power
# print(np.power(a, 2))

# # Square Root
# print(np.sqrt(b))

# # Cube Root
# print(np.cbrt(125))

# # Absolute values
# print(np.absolute(a))

# # Round ---> same as around
# print(np.round(e,2))
# print(np.around(e,2))
# print(np.round(e)) ----> rounds to 0th place

# # Truncation ----> same as Fix
# print(np.trunc(e))
# print(np.fix(e))

# # Floor
# print(np.floor(e))

# # Ceil
# print(np.ceil(e))

# # THIRD CLASS

# c = np.array([1.4, 1.5, 1.6])
# d=b.astype(int)
# print(d)
# e = np.array([1.4, 1.5, 1.6])
# print(c==e)
# print(np.array_equal(c,e))

# a = np.array([[4, 5], [9, 10]])
# b = np.array([[4, 5], [9, 10]])

# # Aggregate functions:

# # 1. Sum
# # Summation of two arrays
# print(np.sum([a,b]))

# # Sum of whole array
# print(np.sum(b))

# # Summation of Rows [axis=0 means row, axis=1 means column]
# print(np.sum(b,axis=0))

# # Summation of Columns
# print(np.sum(b,axis=1))

# # 2. Min
# print(np.min(b))

# # 3. Max
# print(np.max(b))

# # 4. Median
# print(np.median(b))

# # Mean
# print(np.mean(b))


# a = np.array([12, 78, 4, 1, 7, 64, -1, 5])
# b = np.array([[4, 5], [7, 8]])

# # Sorting in ascending order
# print(np.sort(a))

# # Sorting in descending order
# print(np.sort(a)[::-1])

# # Appending in an array
# c = np.array([1,2,3,4,5,6])
# d = np.append(c,7)
# print(d)

# # Deleting (array name, index value, axis) [axis=0 means row, axis=1 means column]

# # Deleting a column
# print(np.delete(b, 0, axis=1))

# # Deleting a row
# print(np.delete(b, 0, axis=0))

# # Reshaping arrays ---> Values should be equally divisible
# print(a.reshape(2,3))
# print(a.reshape(2,2,2))

# # Reshaping arrays from n dimension to 1
# print(b.ravel())

# # Transposing arrays
# print(b.T)

# # FOURTH CLASS

# # All 0s matrix
# c = np.zeros((2, 3))
# print(c)

# # All 1s matrix, You can also specify the data type
# d = np.ones((3, 2), dtype="int16")
# print(d)

# # Matrix of Any other number ((dimension),number)
# e = np.full((2, 3), 19)
# print(e)

# # Another method is by using full_like (array,number)
# f = np.full_like(a, 7)
# print(f)

# # From a range (start,stop-1,step)
# g = np.arange(1,17,2)
# print(g)

# # Dividing elements linearly (start,stop,divisons)
# h = np.linspace(0, 50, 6)
# print(h)

# # Identity matrix
# i = np.identity(5)
# print(i)

# #Iteration
# for k in i.flat:
#     print(k)


# Test:

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([10, 20, 30, 40, 50])
# print(np.sum(np.multiply(arr1,arr2)))


# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# arr1 = arr.reshape(4, 5)
# print(np.mean(arr1), np.std(arr1), np.median(arr1))
# num = np.mean(arr1)
# L=[]
# for i in arr1.flat:
#     if i > num:
#         L.append(1)
#     else:
#         L.append(0)
# print(np.array(L))


# arr4 = random.rand(1000)
# count = 0
# for i in arr4.flat:
#     if i > 0.5:
#         print(i)
#     if i > 0.7:
#         count+=1
# print(count)
# print(np.sort(arr4))
