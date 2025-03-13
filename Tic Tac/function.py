def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end = '')
        print()
def choice_coords(board,player):
    print(f'Ходит игрок {player}')
    print('Введите строку и столбец(счет начинается с 0):')
    row = int(input('Строка:'))
    col = int(input(('Столбец:')))
    step_valid = True
    while step_valid:
        if board[row][col] == '□':
            board[row][col]=player
            step_valid = False
        elif 0<row>2 or 0<col > 2:
            print('Вы вышли за доску.Счет столбцов и строк начинается с 0')
        else:
            print('•Здесь уже занято!•')
            row = int(input('Строка:'))
            col = int(input('Столбец:'))
    return board
def check_board(board):
    if (board[0][0]==board[1][1] == board[2][2]) and board[0][0] != '□':
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != '□':
        return board[0][2]
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board [i][0]!='□':
            return board[i][0]
    for j in range(len(board)):
        if board[0][j] == board[1][j] == board[2][j] and board [0][j]!='□':
            return board[0][j]