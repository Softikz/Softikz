import random
lst=[]
summ = 0
n = int(input('Введите размер списка:'))
for i in range(0,n,1):
    lst.append(random.randint(1,100))
    summ += lst[i]
print(lst)
print(summ)