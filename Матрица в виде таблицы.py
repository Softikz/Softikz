rows = int(input('Кол-во строк:'))
colums = int(input('Кол-во столбцов:'))
matrix = []
for i in range(0, rows, 1):
    row = []
    for j in range(0, colums, 1):
        row.append(0)
    matrix.append(row)
for i in range(0, rows, 1):
    for j in range(0, colums, 1):
        print(matrix[i][j],end='')
    print()
