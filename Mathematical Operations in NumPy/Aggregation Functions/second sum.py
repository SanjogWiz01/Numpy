'''
uint8 and float32 and checks if the result's data type matches np.uint and np.float'''
import numpy as np
s=np.array([1,2,3,4,.5])
print(np.sum(s)) # print all sum
print(np.sum(s,dtype = np.uint8)) # print all sum iin int
print(np.sum(s,dtype = np.float32)) # print all sum as folat
print(np.sum(s).dtype == np.uint) # false as its a float opuput
