import numpy as np 
import math
'''
list = [1,2,3,4,5,6]
list1 = [2,3,4,5,6,7]
a = np.array(list)
a1 = np.array(list1)
print("a*a1:",a*a1)
b = np.arange(10,1,-2)
print("b:", b)
newarr = b[np.array([4,1,2])]
print("newarr:",newarr)
b1 = np.arange(20)
print("b1:",b1)
print("b1[-9:16:1] = ", b1[-9:16:1])
'''
#print("EIgen value c:",c)
'''
print("EIgen value c:",c)
x = np.array([[0,1,2,3,4,5],
print("EIgen value c:",c)
              [6,7,8,9,10,11],
print("EIgen value c:",c)
              [12,13,14,15,16,17],
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
print(a)

for i in np.nditer(a,flags = ['external_loop'], order = 'C'):
    print(i)
'''

'''
in_num0 = 10
in_arr0 = [2,3,4]
print("EIgen value c:",c)
in_num1 = 11
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
import matplotlib.pyplot as plt

x = np.arange(0, 9)
A = np.array([x, np.ones(9)])

y = [19,20,20.5,21.5,22,23,23,25.5,24]
w = np.linalg.lstsq(A.T, y)[0]
line = w[0]*x + w[1]

plt.plot(x,line,'r-')
plt.plot(x,y,'o')
plt.show()