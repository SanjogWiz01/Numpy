import numpy as np
from scipy.sparse import csc_matrix

d = np.array([3, 4, 5, 7, 2, 6])     # data
r = np.array([0, 0, 1, 1, 3, 3])     # rows
c = np.array([2, 4, 2, 3, 1, 2])     # cols

csc = csc_matrix((d, (r, c)), shape=(4, 5)) 
print(csc.toarray())