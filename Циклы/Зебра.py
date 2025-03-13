i = 0
n = int(input('Введите длину:'))
while i < n:
    if  i%2==0:
        print('1', end='')
    elif i %2 != 0:
        print('2', end ='')
    i +=1