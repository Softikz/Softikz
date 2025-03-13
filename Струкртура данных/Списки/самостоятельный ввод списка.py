lst = [3,4,5,6,7,8,9,0]
for i in range(0,len(lst),1):
   print(f'Значение:{lst[i]} Номер:{i}')
lst2=[]
size = int(input('Размер списка'))
for i in range(0,size,1):
    lst2.append(int(input('Элемент списка(числа):')))
print(lst2)