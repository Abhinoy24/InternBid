import numpy as np 
'''
print(np.__version__)
np.show_config
'''

'''
Z = np.zeros(10)
Z[4] = 1
print(Z)
'''

'''

Z = np.arange(10,50)
print(Z)
z = np.arange(50)
z = z[::-1]
print(z)
'''

'''
Z = np.arange(10).reshape(2,5)
print(Z)
'''

'''
nz = np.nonzero([1,2,3,0,0,4,0])
print(nz)

Z = np.eye(3)
print(Z)
'''
'''
Z = np.random.random((3,3,3))
print(Z)
'''

'''
Z = np.random.random((10,10))
Zmin,Zmax = Z.min(),Z.max()
print(Zmin,Zmax)
'''

'''
Z = np.random.random(30)
m = Z.mean()2    d    
print(m)
'''

'''
Z  = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
'''

'''
number = int(input("Enter the range:"))

for i in range(0,number):
    for j in range(0,i):2    d   
        print("",i)
    print()
'''

'''
Z = np.diag(1 + np.arange(4),k=-1)
'''

'''
n = int(input("Enter the value of n:"))
z = np.zeros((n,n),dtype=int)
z[1::2,::2] = 1
z[::2,1::2] = 1
print(z)
'''

'''
print(np.unravel_index(100,(6,7,8)))
'''

'''
z = np.tile(np.array([[0,1],[1,0]]),(4,4))
print(z)
'''

'''
Z = np.random.random((5,5))
Zmax,Zmin = Z.max(),Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
'''

'''
color = np.dtype([("r",np.ubyte,1),
                  ("g",np.ubyte,1),
                  ("b",np.ubyte,1),
                  ("a",np.ubyte,1)])
                  
print(color)
'''

'''
Z = np.dot(np.ones((5,3)),np.ones((3,2)))
print(Z) 
'''

'''
Z =np.arange(11)
print(Z)
Z[(3<Z) & (Z<=8)] *= -1
print(Z)
'''

'''
print(sum(range(5),-1))

from numpy import *

print(sum(range(5),-1))

'''

'''
Z = np.random.uniform(-10,+10,10)
print(np.trunc(Z + np.copysign(0.5,Z)))
'''

'''
Z = np.random.uniform(0,10,10)
print(Z)
print(Z - Z%1)
print(np.floor(Z))
print(np.ceil(Z)-1)
print(Z.astype(int))
print(np.trunc(Z))
'''
'''
Z = np.zeros((5,5))
print(Z)
Z += np.arange(5)
print(Z)
'''

'''
def generate():
    for i in range(10):
        yield i
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)
'''

'''
Z = np.linspace(1,10,12,endpoint=True)[1:-1]
print(Z)
'''

'''
Z =np.random.random(10)
Z.sort()
print(Z)
'''

'''
Z = np.arange(10)
print(Z)
print(np.add.reduce(Z))
print(Z)
'''

'''
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
print(A,B)
equal = np.allclose(A,B)
print(equal)
'''

'''
Z = np.zeros(10)
Z.flags.writeable = False
Z[0] = 1
'''

'''
Z = np.random.random((10,2))
#print(Z)
X,Y = Z[:,0],Z[:,1]
#print(X,Y)
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(R)
print(T)
'''
'''
Z = np.random.random(10)
print(Z)
Z[Z.argmax()] = 0
print(Z)
'''


#important
Z = np.zeros((2,2),[('x',float),('y',float)])
Z['x'],Z['y'] = np.meshgrid(np.linspace(0,1,2),np.linspace(0,1,2))
print(Z)


'''
X = np.arange(10)
Y = X + 0.5
C = 1.0 / np.s
'''