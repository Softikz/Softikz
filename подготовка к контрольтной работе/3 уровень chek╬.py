lst = []
n = int(input('кол во:'))
for i in range(0,n,1):
    lst.append(int(input('введите число:')))
for i in range(0,n,1):
    if (i+1)%3==0:
        print(lst[i])
