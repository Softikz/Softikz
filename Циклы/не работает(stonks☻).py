n = int(input())

r = int(input('Рубли:'))
k = int(input('Копейки:'))

print(r,k)
old = r+k * 0.01

for i in  range(0,n,1):
    r = int(input('Рубли:'))
    k = int(input('Копейки:'))
    new= r+k*0.01
if old > new:
 print('down')
elif old < new:
    print('○up○')
else:
        print('☻stable☻')

old = new