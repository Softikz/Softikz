import random

size = int(input('Введите размер списка:'))
lst=[]
for i in range(0,size,1):
    lst.append(random.randint(0,10))

print(lst)