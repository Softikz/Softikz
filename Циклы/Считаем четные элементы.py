count = 0
a = int(input())
b = int(input())
while a<b:
    if a%2==0:
        count+=1
    a +=13
print(count)