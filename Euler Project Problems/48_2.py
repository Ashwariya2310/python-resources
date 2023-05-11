
import numpy as np
from decimal import Decimal

np.seterr(all='warn')

n = 1000
n1 = np.arange(1, n+1)
print(n1)

sum = Decimal(0)
for i in n1:
    sum += Decimal(i) ** Decimal(i)

print("Sum is", sum)