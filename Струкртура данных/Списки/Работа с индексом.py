import random
lst=[]
n = int(input('Введите размер списка:'))
for i in range(0,n,1):
    lst.append(random.randint(1,9))

print(lst)

for i in range(0,n,1):
    if (i+1)%3==0:
        lst[i]=lst[i]*2

print(lst)
