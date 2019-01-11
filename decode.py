import numpy as np 
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr1 = np.array([[1,1,2],[1,2,3],[2,4,5]])
print(arr)
print("Shape of the array", arr.shape)
print("Shape of the array", arr.dtype)
print("\nArray Sum:\n", arr + arr1)
Sqrt = np.sqrt(arr)
print(Sqrt)
trans = arr.T
print(trans)
