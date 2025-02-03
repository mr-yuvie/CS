# import numpy as np

# a = np.array([[1, 2, 3], [4, 5, 6]], np.float64)
# print(a)

# print(a.ndim)
# print(a.shape)
# print(type(a))
# print(a.dtype)
# print(a.size)


# a = np.array([1, 2, 3, 4, 5])
# print(a[2])
# b = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
#            [[0, 1, 2, 3, 4, 5, 6]]
#            [[-7,-6,-5,-4,-3,-2,-1]]
# # b[r,c]
# print(b[1])
# print(b[:,2])
# print(b[:, 2:7])

# b[0, 2] = 15
# print(b)

# b[:, 3] = [20, 21]
# print(b)

# c = np.array([[[1, 2, 3, 4], [3, 4, 5, 6]], [[5, 6, 7, 8], [7, 8, 9, 10]]])
# c[x,y,z]
# print(c.ndim)
# print(c)
# print(c[1,1,1])
# print(c[:,:,1])
# print(c[:,:,1:3])

# c[0,1,3]=10
# print(c)
# c[:,:,2]=[[10,11],[12,13]]
# print(c)

# a = np.array([[-3, 8], [7, 5]])
# f = np.array([1, 2])
# b = np.array([[4, 5], [9, 10]])
# c = np.array([[[4, 5], [6, 7]], [[8, 9], [10, 11]]])
# d = np.array(
#     [
#         [
#             [[4, 5, 6, 7], [6, 7, 8, 9], [8, 9, 10, 11], [10, 11, 12, 13]],
#             [[8, 9, 10, 11], [10, 11, 12, 13], [16, 17, 18, 19], [18, 19, 20, 21]],
#             [[16, 17, 18, 19], [18, 19, 20, 21], [6, 7, 8, 9], [8, 9, 10, 11]],
#         ],
#         [
#             [[12, 13, 14, 15], [14, 15, 16, 17], [4, 5, 6, 7], [6, 7, 8, 9]],
#             [[16, 17, 18, 19], [18, 19, 20, 21], [12, 13, 14, 15], [14, 15, 16, 17]],
#             [[4, 5, 6, 7], [6, 7, 8, 9], [4, 5, 6, 7], [6, 7, 8, 9]],
#         ],
#         [
#             [[22, 23, 24, 25], [26, 27, 28, 29], [14, 15, 16, 17], [22, 23, 24, 25]],
#             [[30, 31, 32, 33], [34, 35, 36, 37], [14, 15, 16, 17], [22, 23, 24, 25]],
#             [[12, 13, 14, 15], [14, 15, 16, 17], [22, 23, 24, 25], [26, 27, 28, 29]],
#         ],
#     ]
# )
# print(np.delete(d, 2))
# (3,3,4,4)
# print(d[1, 1, 3, 2])
# print(d.shape)

# # Math Functions --> Both numbers and arrays are viable arguments. (a,b)

# Addition

# print(np.add(a, f))
# print(np.subtract(a,2))
# print(np.multiply(a,2))

# print(np.divide(a,2))
# print(np.mod(a,2))
# print(np.divmod(a,2)) --> Q, R

# Expon
# print(np.power(a,f))
# print(np.sqrt(b))
# print(np.cbrt(b))

# print(np.absolute(a))

# Estimate
# e = np.array([[1.278, 2.345], [3.954, 4.784]])
# print(np.round(e,1))

# print(np.trunc(e))
# print(np.floor(e))
# print(np.ceil(e))

# Aggregate functions
# 100.2, 500.4, 1000.6
# 1 , 1.278 , 2

# Summation
# print(np.sum(a))
# print(np.sum([a,b]))

# [[-3, 8], [7, 5]]
# axis=0, Row, axis=1, Col
# -3, 7
# 8, 5

# print(np.sum(a,axis=1))

# a = np.array([[-3, 8], [7, 5]])

# print(np.cumsum(a))
# f = np.array([1, 2])
# d = np.array(
#     [
#         [[[4, 5], [6, 7]], [[8, 9], [10, 11]]],
#         [[[12, 13], [14, 15]], [[16, 17], [18, 19]]],
#     ]
# )
# b = np.array([[4, 5], [9, 10]])
# c = np.array([[[4, 5], [6, 7]], [[8, 9], [10, 11]]]) #1,8 2,2,2 4,2 2,4 8,1

# reshape, m%n=0

# print(d.reshape(2,2,4))
# 16: 1,16 2,8 4,4 8,2 16,1
# 2,2,4 2,2,2,2

# 10: 1,10, 2,5 5,2 10,1

# print(np.ravel(d)) nd--> 1D
# print(c.reshape(2,2,4))

# Min
# 4, 9
# 5, 10
# print(np.min(b,axis=0))
# print(np.max(b,axis=0))
# print(np.mean(b))
# print(np.median(c))
# print(np.std(b))

## Sorting
# a = np.array([12, 78, 4, 1, 7, 64, -1, 5])
# b = np.array([[4, 5], [7, 8]])

# start:stop:step
# print(np.sort(a)[::-1])

# n=int(input("Value:"))
# L=[]
# for i in range(n):
#     L.append(i)
# g = np.array(L)
# print(g)

# num = int(input("Enter total numbers: "))
# arr = np.array([], np.int64)
# for i in range(num):
#     arr = np.append(arr, i)
# print(arr)

# a = np.array([12, 78, 4, 1, 7, 64, -1, 5])
# b = np.array([[4, 5], [7, 8]])
# axis=0:Row, axis=1,Colu
# b[1,0]=0
# 4 7
# 5 8

# 0 matrix
# 0 0
# 0 0

# Identity matrix

# 1 0 0
# 0 1 0
# 0 0 1

# a = np.zeros((2,2))
# print(a)

# b = np.full((2,2), 79)
# print(b)

# g =np.arange(1,17).reshape(2,2,2,2)
# print(g)

# i = np.multiply(np.identity(4),5)
# print(i)

# m = np.arange(0,50,6)
# h = np.linspace(0,128,6)
# print(h)
# print(m)

# d = np.array(
#     [
#         [[[4, 5], [6, 7]], [[8, 9], [10, 11]]],
#         [[[12, 13], [14, 15]], [[16, 17], [18, 19]]],
#     ]
# )

# for i in np.ravel(d):
#     print(i)
