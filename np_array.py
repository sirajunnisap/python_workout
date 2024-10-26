import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,0])
# print(arr)

# print(arr[1:7:2])
# print(arr[:8:2])

arr2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr2D)
# print(arr2D[0:2,0:3:2])

# no. of Dimentsion
# print(arr2D.ndim)

# no. of elements in each dimention here 2D have 2 element 1D have 5 elements
# print(arr2D.shape)


arr3D = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,22,33],[44,55,66],[77,88,99]]])
print(arr3D)
print(arr3D[1,2,0:2])
reshaped1 = arr3D.reshape(-1)
reshaped2 = arr3D.reshape(3,6)
print(reshaped1)
print(reshaped2)