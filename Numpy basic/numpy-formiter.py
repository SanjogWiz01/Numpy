import numpy as np

sanjog= "sanjogpoudelisdonofnumpy"

arr = np.fromiter(sanjog, dtype = 'U2')

print("fromiter() array :",
      arr)
# Syntax: numpy.fromiter(iterable, dtype, count=-1)