import random
f=0
lst = []
size = 100
for i in range(0,100,1):
    lst.append(random.randint(-5, 5))
    if lst[i]>0:
        lst[i]='+'
        f+=1
    else:
        lst[i] = '-'

print(lst)
print(f)

