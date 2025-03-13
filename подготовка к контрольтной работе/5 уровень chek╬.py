import random
lst = []
for i in range(0,100,1):
    lst.append(random.randint(0,5))
for i in range(0,100,1):
    if lst[i]%2==0 and i%2!=0:
        print(i)
print(lst)
