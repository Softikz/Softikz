import random
lst = []
for i in range(0,100,1):
    lst.append(random.randint(1,9))
print(lst)
a= int(input('число'))
b = int(input('число'))
summ = 1
for i in range(0,100,1):
    if a <= i <= b:
        summ *=lst[i]
print(summ)
