import numpy as np
#2 input 3d arrays

m=np.array([[[1,2,3],
            [4,5,6],
            [7,8,9]],

            [[10,11,12],
            [13,14,15],
            [16,17,18]]])

n=np.array([[[51,52,53],
            [54,55,56],
            [57,58,59]],

            [[110,111,112],
            [113,114,115],
            [116,117,118]]])

# stacking with axiux 0 1 2 3
q=np.stack((m,n),axis=0)
w=np.stack((m,n),axis=1)
e=np.stack((m,n),axis=2)
r=np.stack((m,n),axis=3)
t=np.row_stack((m,n))
y=np.column_stack((m,n))
print('DATA ARE :\n',q,w,e,r,t,y)
