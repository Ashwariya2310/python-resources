a=1
b=2
l=[a, b]
def fib(a, b, l):
    sum=0
    c=0
    for i in range(2, 10000):
        c=a+b
        if c<=4000000:
            l.append(c)
        else:
            break
        a=b
        b=c
    return l

        
    

fib_series= fib(a, b, l)

def iseven(series):
    sum=0
    for j in series:
        if j%2==0:
            sum+=j

    return sum

even = iseven(fib_series)

print(f"Sum is {even}")




