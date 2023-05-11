#sum of multiple of 3 or 5 below 1000


my_set= set()
def mul(): 
    for i in range(1, 10):
        if i%3 ==0 or i%5==0:
            my_set.add(i)

    return my_set

set_of_mul= mul()

def sum(sett):
    s=0
    for i in sett:
        s+=i
    return s

score= sum(set_of_mul)
print(f"Sum is {score}")