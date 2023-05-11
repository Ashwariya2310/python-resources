import math
import numpy as np
np.seterr(all='warn')
n=1000
n1= np.arange(501, n+1)

sum=0
for i in n1:
    sum+=i**i

print("Sum is ", sum)

    