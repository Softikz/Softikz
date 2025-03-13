lst = []
n = int(input('Введите кол во:'))
for  i in range(0,n,1):
    lst.append(int(input('введите теперь число:')))
summ = 0
for i in range(0,n,1):
    if lst[i]%3==0:
        summ += lst[i]
print(summ)