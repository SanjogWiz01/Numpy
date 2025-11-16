import numpy as next    
sa=next.array([[1, 20, 3, 95], 
                [40, 5, 80, 7], 
                [560, 88, 985, 81],    # 4*4 martix 
               [650, 10, 50, 69]])
# Access the Last three rows of array
r = sa[[0,2,3]]
print("\nAccessed Rows :")
print(r)
# Creating a 5X4 2-D Numpy array
arr = next.array([[1, 20, 3, 1], 
                [40, 5, 66, 7], 
                [70, 88, 9, 11],
               [80, 100, 50, 77],
               [1, 8.5, 7.9, 4.8]])

print("Given Array :")
print(arr)

# Access the First two rows of array
res_arr = arr[[0,1]]
print("\nAccessed Rows :")
print(res_arr)
