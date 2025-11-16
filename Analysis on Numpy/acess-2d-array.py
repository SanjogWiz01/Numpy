import numpy as np
arr1=np.array([[10, 20, 30], 
                [40, 5, 66], 
                [70, 88, 94]])

print('ll array before,arr1 is\n',arr1)
arr2=arr1[[0,1]]
print('acces to\n',arr2)
a=arr1[1]
print("\nAccessed Row :")
print(a)