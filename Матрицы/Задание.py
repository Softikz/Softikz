import random
rows = int(input('высота:'))
colums =  int(input('ширина:'))
matrix = []
for i in range(0, rows, 1):
    row = []
    for j in range(0, colums, 1):
        row.append(random.randint(0,10))
    matrix.append(row)


for i in range(0, rows, 1):
    for j in range(0, colums, 1):
            print(matrix[i][j], end=' ')
    print()

print()

for i in range(0, rows, 1):
    for j in range(0, colums, 1):
        if i == j:
            print(matrix[i][j])
    print()
