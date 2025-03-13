import random
lst = []
size = 100
for i in range(0,size,1):
    lst.append(random.randint(0,9))
summ = 0
for i in range(0,size,1):
    if i >=20 and i<=40:
        summ += lst[i]
print(summ/20)