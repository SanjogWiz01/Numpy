import numpy as np
x=np.array([[1,2,3],
            [4,5,6]])
y=np.array([[7,8,9],
            [10,11,12]])
z=np.array([[13,14,15],
            [16,17,18]])   # with axis 0 1 2 

q=np.stack((x,y,z),axis=0)
print(q)
a=np.stack((x,y,z),axis=1) # row attack coc
print('ROW WIZE: \n',a)
w=np.stack((x,y,z),axis=2)
print ('column attack ishere tooo :\n',w)
