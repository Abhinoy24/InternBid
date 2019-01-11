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
'''
x = np.array([[0,1,2,3,4,5],
              [6,7,8,9,10,11],
              [12,13,14,15,16,17],
              [18,19,20,21,22,23],
              [24,25,26,27,28,29],
              [30,31,32,33,34,35]])
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
in_num1 = 11
in_arr0 = [2,3,4]

out_num = np
in_arr0 = [2,3,4]num0,in_num1)
print(out_ar
in_arr0 = [2,3,4]
print("bitwi
in_arr0 = [2,3,4] 11: ",out_num)
'''
'''
print(out_arr)
in_arr0 = [2,3,4]
print(out_arr)
print(out_arr)
in_arr0 = [2,3,4]
in_arr1 = [3,5,6]

print(out_arr)
out_arr = np.bitwise_and(in_arr0,in_arr1)
print(out_arr)
print(out_arr)
out_arr = np.bitwise_or(in_arr0,in_arr1)
print(out_arr)
'''
'''
in_arr = [0,math.pi,np.pi,math.pi/2,np.pi/2]
print(in_arr)
'''
'''

in_arr1 = [0,30,45,60,90]
sin_value = np.sin(in_arr1)
cos_value = np.cos(in_arr1)
tan_value = np.tan(in_arr1)
print(sin_value)
print(cos_value)
print(tan_value)
'''
teststring = "Aishwarya is the Gang"
result = np.char.split(teststring, sep = 'i')
print(result)
result = np.char.join('*',teststring)
print(result)
result = np.char.upper(teststring)
print(result)
result = np.char.count('i',teststring)
print(result)
result = np.char.join('-',teststring)
