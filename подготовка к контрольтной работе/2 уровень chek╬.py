import random
lst = []
for i in range(0,100,1):
    lst.append(random.randint(0,10))
for i in range(0,100,1):
    lst[i]-= 100

print(lst)
