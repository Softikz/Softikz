a = int(input('Введите число а:'))
b = int(input('Введите число б:'))
if a<b:
    while a<b+1:
        print(a)
        a+=1

elif a>b:
    while a>b-1:
        print(a)
        a-=1
else:
    print('error')