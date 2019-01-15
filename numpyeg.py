import numpy as np 
import math
'''
list = [1,2,3,4,5,6]
list1 = [2,3,4,5,6,7]
a = np.array(list)
a1 = np.array(list1)
print("a*a1:",a*a1)
b = np.arange(10,1,-2)
print()
print("b:", b)
print()
newarr = b[np.array([4,1,2])]
print()
print("newarr:",newarr)
print()
b1 = np.arange(20)
print()
print("b1:",b1)
print()
print("b1[-9:16:1] = ", b1[-9:16:1])
'''
#print("EIgen value c:",c)
'''
print("EIgen value c:",c)
x = np.array([[0,1,2,3,4,5],
print("EIgen value c:",c)
print()
              [6,7,8,9,10,11],
print()
print("EIgen value c:",c)
print()
              [12,13,14,15,16,17],
print()
print("EIgen value c:",c)
              [18,19,20,21,22,23],result = np.char.join('-',teststring)
print("EIgen value c:",c)
print("EIgen value c:",c)
print("EIgen value c:",c)
              [24,25,26,27,28,29],result = np.char.join('-',teststring)
print("EIgen value c:",c)
print("EIgen value c:",c)
              [30,31,32,33,34,35]]result = np.char.join('-',teststring)
print("EIgen value c:",c)
print("EIgen value c:",c)
print("EIgen value c:",c)
#print(x)
#print(x[0,:])
#print(x[0,3:5])
#print(x[4:, 4:])
print(x[1::2,::2])
'''


'''
print()
b = np.array([[[1, 2, 3],[4, 5, 6]],
              [[7, 8, 9],[10, 11, 12]]])
result = np.char.join('*',teststring)
print(b)
'''

#print("EIgen value c:",c)
#in_arr0 = [2,3,4]
'''
a = np.arange(12)
result = np.char.join('*',teststring)
print(a)
result = np.char.join('*',teststring)
a = a.reshape(3,4)
result = np.char.join('*',teststring)
print()
print(a)

for i in np.nditer(a,flags = ['external_loop'], order = 'C'):
    print(i)
'''

'''
in_num0 = 10
in_arr0 = [2,3,4]
print()
print("EIgen value c:",c)
in_num1 = 11
print()
print("EIgen value c:",c)
in_arr0 = [2,3,4]

print("EIgen value c:",c)
out_num = npresult = np.char.join('-',teststring)
in_arr0 = [2result = np.char.join('-',teststring)
print(out_arresult = np.char.join('-',teststring)
in_arr0 = [2result = np.char.join('-',teststring)
print("bitwiresult = np.char.join('-',teststring)
in_arr0 = [2result = np.char.join('-',teststring)
'''
'''
print(out_arr)
in_arr0 = [2,3,4]
print(out_arr)
print(out_arr)
in_arr0 = [2,3,4]
in_arr1 = [3,5,6]

print(out_arr)result = np.char.join('-',teststring)
out_arr = np.bitwise_and(in_arr0,in_arr1)
print(out_arr)
print(out_arr)
out_arr = np.bitwise_or(in_arr0,in_arr1)
print(out_arr)
in_arr = [0,math.pi,np.pi,math.pi/2,np.pi/2]
print(in_arr)
'''

'''

print("EIgen value c:",c)
in_arr1 = [0,30,45,60,90]result = np.char.join('-',teststring)
print("EIgen value c:",c)
sin_value = np.sin(in_arr1)
cos_value = np.cos(in_arr1)
tan_value = np.tan(in_arr1)
print("EIgen value c:",c)
print(sin_value)
print("EIgen value c:",c)
print(cos_value)
print("EIgen value c:",c)
print("EIgen value c:",c)
print(tan_value)
print("EIgen value c:",c)
'''

'''
result = np.char.join('-',teststring)
tesresult = np.char.join('-',teststring)"
resresult = np.char.join('-',teststring)sep = 'i')
priresult = np.char.join('-',teststring)
result = np.char.join('*',teststring)
print(result)
result = np.char.upper(teststring)
print(result)
print("EIgen value c:",c)
'''

'''
print("EIgen value c:",c)
a = np.array(['Aishwarya','Ruchita','Panna','Preksha','Tejaswini'])
print("EIgen value c:",c)
result = np.char.count(a,'Panna')
print("EIgen value c:",c)
print(result)result = np.char.join('-',teststring)
print("EIgen value c:",c)
'''

'''
#instead of unequal use not_equal
a1 = np.char.not_equal('test','cat')
print(a1)
a = np.char.greater('test','cat')
print(a)

'''

'''
A = np.array([[6,1,1],[4,-2,5],[2,8,7]]) 
print(A)
print("RANK of A: ", np.linalg.matrix_rank(A))
print("Matrix A raised to the power 2 ", np.linalg.matrix_power(A,2))

'''

'''
from numpy import linalg as geek
a = np.array([[1,-2j],[2j,5]])
print("ARRAY IS : ", a)

c, d = geek.eigh(a)

print("EIgen value c:",c)
print("EIgen value d:",d)
'''

'''
a = np.array([[1,2],[3,4]])
b = np.array([8,18])
x = np.linalg.solve(a,b)
print(x)
'''


'''
import matplotlib.pyplot as plt

x = np.arange(0, 9)
A = np.array([x, np.ones(9)])

y = [19,20,20.5,21.5,22,23,23,25.5,24]
w = np.linalg.lstsq(A.T, y)[0]
line = w[0]*x + w[1]

plt.plot(x,line,'r-')
plt.plot(x,y,'o')
plt.show()

'''

'''

a = np.array([9,3,14,5,6,7])
print("Original Array:",a)

b = np.argsort(a)
print("Sorted array:",b)

c = np.zeros(len(b),dtype = int)
for i in range(0,len(b)):
    c[i] = a[b[i]]
print("Sorted Array:",c) 

'''

'''
a = np.array([9,3,2,4,5,1,6])
b = np.array([8,4,5,6,1,2,7])

for(i,j) in zip(a,b):
    print(i,'',j)
ind = np.lexsort((b,a))
print(ind)

'''

'''
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print("Vertical Stacking :", np.vstack((a,b)))
print("Horizontal Stacking:", np.hstack((a,b)))

'''

'''
a = np.array([1,2,3,4,5,6])
print("Adding 1 to each element :",a+1)
print("Subtracting 2 from each element:",a-2)
print("Mulitplying 2 with each element:",a*2)
print("Squaring each element:",a**2)
a*=2
print("Modified Array:",a)
b = np.array([[1,2],[3,4],[5,6]])
print(b)
print(b.T)
'''

'''
a = np.array([[1,3,5],[7,9,11],[13,15,17]])
print("Largest Element is : ", a.max())
print("Row Wise Largest Element:",a.max(axis = 1))
print("Column Wise Largest Element:",a.max(axis = 0))
print("Sum of all Array ", a.sum())
print()
print("Cumulative Sum of each row ", a.cumsum(axis = 1))
print()
print("Cumulative Sum of each column ", a.cumsum(axis = 0))
print()
'''

'''
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
drop
drop
drop
drop
print()
print("Matrix Multiplication: ", a.dot(b))
print()

a1 = np.array([0,1,2,3])print()

print("Exponent of array elements:",np.exp(a1))
print("Sine of array elements:",np.sin(a1))

'''

'''
a = np.array([[1,3,2],[-1,0,5],[6,9,10]])
print(a)
print("Sorted array:", np.sort(a,axis=None))
print("Row Wise SOrted Array: ", np.sort(a,axis=1))
print("Column Wise SOrted Array: ", np.sort(a,axis=0,kind='MergerSort'))

'''


dtypes = [('name',np.unicode_, 16),('grad_year',int),('CGPA',float)]
values = [('Aroj',2019,9.8),('Abhik',2019,8.4),('Kiwi',2019,8.4),('Nima',2019,7.5)]

arr =np.array(values,dtype = dtypes)
print(arr)
print()
print("Sorted Order w.r.t name:",np.sort(arr,order='name'))
print()
print("Sorted Order w.r.t Cgpa:",np.sort(arr,order='CGPA'))
print()


'''
print()drop


x,y = inpudrop
print("First Number is {} and Second Number is {}".format(x,y))
print()
print()
print()
print("Number of boys:",x)
print()
print("Number of Girls:",y)
print()
print()
print()
y = list(map(int, input("Enter a multiple values:").split()))
print()
print("List of Prices:",y)

'''

'''
a = [1,2,3,4]
print()
try:
    print("Second Element:%d",a[1])
    print("Fifth Element:%d",a[4])
except IndexError:
    print("An Error Occured")
'''

'''
def divide(x, y):
    try:
print()
        result = x//y
print()
print()
        print("ANSWER IS :",result)
print()
print()
print()
    except ZeroDivisionError:
print()
print()
        print("Error Division of Zero")

divide(1,2)
divide(3,2)
divide(1,0)

'''

'''
def Merge(list1,list2):
    check_list = list1 + list2
    check_list.sort()
    return(check_list)

list1 = ['Abhinoy','Aishwarya','Vishal']
list2 = ['Abhik','pradip','Nima']          
new_list = Merge(list1,list2)
print(new_list)
'''

'''

import random

list = [1,3,5,[(b7,9,11,13,15,17,19]
[(b
print("List be[(bfore Shuffling:",end="")
for i in range[(b(0,len(list)):
    print(list[i],end=" ")
print("\r")

print("List after Shuffling:",end=" ")
random.shuffle(list)
for i in range(0,len(list)):
    print(list[i],end=" ")
print("\r")

'''
'''
def printcheckboard(n):
    print("Checkboard Pattern:")
    x = np.zeros((n,n), dtype = int)
    x[1::2,::2] = 1
    x[::2,1::2] = 1
    for  i in range(n):
        for j in range(n):
            print(x[i][j],end=" ")
        print()
n = int(input("Enter the value of n???"))
printcheckboard(n)

'''