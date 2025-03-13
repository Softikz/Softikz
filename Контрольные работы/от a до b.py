a = int(input('Введите чиcло 1:'))
b = int(input('Введите чиcло 2:'))
for i in range(a,b+1,1):
    if a<b:
        print(i,end= ' ')
    else:
        print('число 1 должно быть меньше числа 2')