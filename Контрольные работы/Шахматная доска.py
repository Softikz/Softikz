size = int(input())
for i in range(size):
    if i%2==0:
        print(size//2*'□■')
    else:
        print(size//2*'■□')