import random
lst = []
for i in range(0,100,1):
    lst.append(random.randint(-10,10))
for i in range(0,25,1):
    if lst[i]%3==0:
        lst[i]=0
print(lst)
