# import numpy as np

# arr = np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]])
# print(arr)

# print(arr.ndim)

#arr=np.array([1,2,3,4,5,6,7])
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#print(arr[-3:-1:2])
# print(arr[0:2, 1:4])

# import numpy as np

# #arr = np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]])
# arr = np.array([[1, 2, 3, 4, 5],[1,2,3,4,5]])
# new=np.array([[1,2,3,4,5],[1,2,3,4,5]])
# arr_f=np.concatenate((arr,new))
# print(arr_f)

# arr = np.array([[3, 2, 4], [5, 0, 1]])

# print(np.sort(arr))

#makes a 2d array with 3 rows and 5 columns with random values between 0-100
# x=np.random.randint(100,size=(3,5))
# print(x)


#indexing 2d array
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[0, 1])

#3d Array INdexing below
# arr=np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]])
# print(arr[0,1,0])

#Slicing 2d lists

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# from 1 List elements 1 to 4 whic his 3 elements including 1,2,3
# print(arr[1, 1:4])

#slicing 2d lists

# slicing the main lists with 0:2 so it returns both the inner lists complete and then getting those lists element 2, Truly a smart way to slice, initial slice and final slice
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:2, 0:2])
########################

# arr=np.array([1,2,3,4,5])
# print(arr.dtype)
# ar=np.array(['a','b','c','d','e'])
# print(ar.dtype)
# dtype prints the type of array that you have created


# arr.shape return number on lists follwing dimensions
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr.shape)#output (2,5) means 2 lists and 5 elements in each multiply everything 10 elements total
# reshape is same as well

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)# Reshape 1 dimension to 4 arrays with 3 elemts in each total 12 elements
# newarr=arr.reshape(2,3,2)# 2 initial lists, inside 3 more lists with 2 elements in each
# print(newarr)


# effectively iterating through np lists

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#     print(x)
#returns real values of all the lists without using for loop again and again

# joining numpy arrays
#np.concatentate is used normally but for easiness we use stack, hstack for stack along rows and vstack for along columns dstack for 3d stuff
# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr=np.hstack((arr1,arr2))

# print(arr)
# axis provides a way to combine lists of 2d and show them as one, normlaly axis is 0 in that case everything is shows as it is no combining

#np.random.randint(100) for random integer between 0-100 and np.random.randint(100,size=(5))means list with 5 elements and random number between 0-100
# x=np.random.randint(100, size=(2,2,10))
# print(x)
#np.random.randint(100,size=(2,2)) means 2 list with 2 elements each and so on with 3d elements