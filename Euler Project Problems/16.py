"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""

n=2
powered=n**1000
s=0
r=0
print("power", powered)
while powered>0:
    r=powered%10
    print("rem",r)
    s=s+r
    print("sum", s)
    powered=powered//10

print("result",s)