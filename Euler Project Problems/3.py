#largest prime factor
import math
n = int(input("Enter no: "))

def isprime(no):
    c=0
    for i in range(1, int(math.sqrt(no))+1):
        if no%i==0:
            c=c+1
    if c==1:
        return True
    else:
        return False

def factors(n):
    factors=[]
    for i in range(2, int(n/2)+1):
        if n%i ==0:
            booll= isprime(i)
            print(f'No is {i}: {booll}')
            if booll==True:
                factors.append(i)
    return factors

fac= factors(n)

print('Prime Factors are: ', fac)



# k=[]

# for j in fac:
#     if isprime(j):
#         k.append(j)

# print('List of Prime factors', k)

fac.sort()

print('Largest ', fac[-1])




