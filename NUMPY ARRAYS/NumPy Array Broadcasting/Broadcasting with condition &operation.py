import numpy as np
# who can come on gen_z fight
age=np.array([10,12,45,15,24+45,78,19,2+3])
group=np.array(['gen_z','not_genz'])
data=np.where(age>12,group[0],group[1])
print(data)