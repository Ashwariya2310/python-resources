n=13
step=1
d=dict()
for n in range(3, 1000000):
    k=str(n)
    step=1
    while n>1:
        step=step+1
        if n%2==0:
            n=n//2
        else:
            n=(3*n)+1

    d[k]=step
    print(d)



sorted_dict = dict(sorted(d.items(), key=lambda x: -x[1]))

# print sorted dictionary
ke=sorted_dict.keys()
print(ke)