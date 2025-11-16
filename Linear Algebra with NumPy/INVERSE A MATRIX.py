import numpy as np
'''
=>Ax=B
=>A 
−1
 Ax=A 
−1
 B
=>x=A 
−1
 B

where,
A-1: The inverse of matrix A
x: The unknown variable column
B: The solution matrix'''
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
print(np.linalg.inv(A)) # Finding inverse of matrix A
A2 = np.array([[6, 1, 1, 3],
              [4, -2, 5, 1],
              [2, 8, 7, 6],
              [3, 1, 9, 7]])
print(np.linalg.inv(A2))