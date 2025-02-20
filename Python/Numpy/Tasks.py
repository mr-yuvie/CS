import numpy as np

# Q1. Write a program to take input from the user of a 1D array and perform basic arithmetic operations
# on it as per the user choice and from the user's given number.
# For eg. If user entered = [1,2,3,4,5] then chose add then entered 2, result should be [3,4,5,6,7]

# num = int(input("Enter total numbers: "))
# arr = np.array([], np.int64)
# for i in range(num):
#     j = int(input("Enter a number: "))
#     arr = np.append(arr, j)

# # num = int(input("Enter total numbers: "))
# # L = []
# # for i in range(num):
# #     j=int(input("Enter a number: "))
# #     L.append(j)
# # arr = np.array(L)

# print(arr)

# choice = int(input("Enter choice (1=Add,2=Sub,3=Multiply,4=Divide): "))

# if choice == 1:
#     num_add = int(input("Number to Add: "))
#     print(np.add(arr, num_add))
# elif choice == 2:
#     num_sub = int(input("Number to Subtract: "))
#     print(np.subtract(arr, num_sub))
# elif choice == 3:
#     num_mul = int(input("Number to Multiply: "))
#     print(np.multiply(arr, num_mul))
# elif choice == 4:
#     num_div = int(input("Number to Divide: "))
#     print(np.divide(arr, num_div))
# else:
#     print("Wrong Choice")

# 1. How would you create a one-dimensional NumPy array of the numbers from 10 to 100, counting by 10?

# expected output: [10,20,30,40,50,60,70,80,90,100]

# array = np.array([],dtype=int)
# for i in range(10,110,10):
#     array = np.append(array,i)
# print(array)

# 2. Following is the provided numPy array. Return array of items by taking the third column from all rows:
# sampleArray = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# expected ouput: [33 66 99]
# sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
# print(sampleArray[:,2])

# 3. Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element
# arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
# arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

# expected output:
# addition of two arrays is

# [[20 39 33]
#  [25 25 28]]

# Result array after calculating the square root of all elements

# [[ 400 1521 1089]
#  [ 625  625  784]]

# arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
# arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
# added_array = np.add(arrayOne,arrayTwo)
# print(added_array)
# result = np.power(added_array,2)
# print(result)

# 4. Print max from axis 0 and min from axis 1 from the following 2-D array.
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

# expected output:
# Printing a min Of Axis 1
# [34 12 53]

# Printing a max Of Axis 0
# [82 94 73]

# sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
# print(np.min(sampleArray,axis=1))
# print(np.max(sampleArray,axis=0))
