'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''
import math
def isprime(no):
    c=0
    for i in range(1, int(math.sqrt(no))+1):
        if no%i==0:
            c=c+1
    if c==1:
        return True
    else:
        return False
num=2000000
s=0
for i in range(2, num):
    if isprime(i):
        print(i)
        s+=i
        print(s)
    
print(f"sum: {s}")
