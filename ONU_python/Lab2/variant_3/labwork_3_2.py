import numpy as np
import math

ar1 = np.array([[6,5,4,3,2,1]])
ar2 = ar1 * -1
ar3 = np.tile(np.array([[2,2],[2,2],[4,4],[4,4]]),3)
block_array = np.concatenate([ar1,ar2,[ar3[0]],[ar3[1]],[ar3[2]],[ar3[3]]],axis=0)

oldelem = math.inf
for i in range(6):
    for j in range(6):
        oldelem = min((block_array[i][j])**3,oldelem)
print(oldelem)
