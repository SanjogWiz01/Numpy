import numpy as np

arr = np.array([10, 15, 20, 25, 30])

print(arr[arr >= 20]) # print the array above confiton 
arr = np.array([10, 15, 20, 25, 30])

print(arr[(arr > 10) & (arr < 30)]) # works as gate