import random
lst=[]
n = int(input('Введите размер списка:'))
for i in range(0,n,1):
    lst.append(random.randint(1,100))
    if lst[i] > 50:
        lst[i]=50
print(lst)