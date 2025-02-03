import numpy as np
from numpy import random

# import statistics as st

# a = np.array([[-3, -8], [7, -5]])
# b = np.array([[4, 5], [9, 10]])

# e = np.array([[1.278, 2.345], [3.954, 4.784]])
# f = [4, 9, 16]

# mathematical functions:
# 3 parts ---> Arithmetic, Exponetinal, Estimate
# np.func(a,b) ---> Both numbers and arrays are viable arguments.

# Arithemetic:
# # Addition
# print(np.add(a,2))

# # Subtraction
# print(np.subtract(a,b))

# # Multiplication
# print(np.multiply(a,1.0))

# Division
# np.divide --> division
# np.mod ---> Remainder
# np.divmod ---> Qoutient,Remainder

# # Exponentinal --> **
# power--> np.power(a,b)
# sqrt --> np.sqrt(a)
# cbrt --> np.cbrt(a)

# print(np.sqrt(f))

# # Estimate

# Trunc/Fix --> truncate (removal/deletion)
# print(np.trunc(e))
# print(np.fix(e))

# round <--> around (np.round(a,b)): a is the array, b is the nth place of decimal
# print(np.around(e,2))
# print(np.around(e))

# # Floor
# print(np.floor(e))

# # Ceil
# print(np.ceil(e))

# print(np.absolute(a))

# # Performing operations on arrays with different dimensions
# print(np.divide(b, c))
# print(np.divide(c,b))
# b,c --> 4/8, c,b --> 8/4 , 3D > 2D > 1D > 0D


# # Another way of type casting
# b= np.array([1,2,3,4])
# c = b.astype(float)
# print(c)

# a =np.array([1,2,3,4,5])
# b =np.array([1,2,3,4,5])

# # print(a==b) # Element wise comparison

# # print(np.array_equal(a,b)) # array equality

# if(np.array_equal(a,b)):
#     print("Data is same")

# # Aggregate functions

# # Sum
# print(np.sum(a))
# print(np.sum([a,b]))

# Rows[axis=0] and Columns[axis=1]:
# a = np.array([[4, 5], [9, 10]])
# b = np.array([[4, 5], [9, 10]])

# # a:
# # [4,9]
# # [5,10]
# print(np.sum(a,axis=0))

# # Minimum(Min)
# print(np.min(a,axis=0))

# # Max
# print(np.max(b,axis=0))

# # Mean
# print(np.mean(a))

# # Median
# print(np.median(a))

# # Standard deviation
# print(np.std(a))

# a = np.array([12, 78, 4, 1, 7, 64, -1, 5])
# b = np.array([[4, 5, 3], [7, 8, 2]])
# c = np.array([[[8, 10], [18, 30]], [[8, 45], [27, 100]]])
# d = np.array(
#     [
#         [[[4, 5], [6, 7]], [[8, 9], [10, 11]]],
#         [[[12, 13], [14, 15]], [[16, 17], [18, 19]]],
#     ]
# )

# b:
# [4] [7]
# [5] [8]
# [3] [2]

# b:
# [4,5,3]
# [7,8,2]

# # Sort
# print(np.sort(b, axis=1))
# print(np.sort(a)[::-1])

# # Append
# c = np.append(b,[1,2])
# print(c)

# print(np.sort(c))

# # Deletion

# print(np.delete(b,0,axis=1))
# print(np.delete(b,0,axis=0))
# # transpose: axis= interchange
# print(b.T)

# # Reshape: a, n --> m: nummber of elements of n should be disvisble by m, ravel: n --> 1
# print(np.ravel(d)) # flat

# print(d.reshape(2,2,2,2)) #16,1 , 1,16, 2,8, 8,2 4,4
# print(d.size)


# #Array generate
# All 0 matrix
# a = np.zeros()
# print(a)

# b = np.ones((3,3),dtype=int)
# print(b)
# num =10

# c = np.arange(1,num)
# print(c)

# a="Hello129Bye"
# for i in a:
#     if i.isalpha():
#         count+=1
#     elif i.isnumeric:
#         count_num+=1

# # Matrix of Any other number ((dimension),number)
# e = np.full((2, 3), 79)
# print(e)

# f = np.identity(5)
# print(f)

# from numpy import random

# L = random.rand(3, 5)
# print(L)

# for i in f.flat:
#     print(i)
