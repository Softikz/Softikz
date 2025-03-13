import random
lst = []
for i in range(0,25,1):
    lst.append(random.randint(-5,5))
for i in range(0,25,1):
    if lst[i]<0:
        lst[i]=0
print(lst)