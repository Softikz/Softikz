lst =[]
summ = int(input(':'))
n = int(input('6'))
for i in range(0,n,1):
    lst.append(int(input(':')))
    if (i+1)%3==0:
     summ+=lst[i]
print(summ)