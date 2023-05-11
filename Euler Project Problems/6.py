'''The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

n=100
diff=0
def sq_o_sum(n):
    s=0
    for i in range(1, n+1):
        s+=i**2
    return s

sq=sq_o_sum(n)
def sum_o_sq(n):
    s=0
    for i in range(1, n+1):
        s+=i
    return s**2
summ=sum_o_sq(n)
if sq>=summ:
    diff=sq-summ
else:
    diff=summ-sq

print(diff)


import numpy as np

n = 100

def sq_o_sum(n):
    return np.sum(np.arange(1, n+1)**2)

def sum_o_sq(n):
    return np.sum(np.arange(1, n+1))**2

sq = sq_o_sum(n)
summ = sum_o_sq(n)

diff = np.abs(sq - summ)
print(diff)