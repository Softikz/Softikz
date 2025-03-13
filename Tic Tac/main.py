import function
board = [
    ['□','□','□'],
    ['□','□','□'],
    ['□','□','□'],
]
run = True
step = 0
while run:
    function.print_board(board)
    if step %2==0:
        board = function.choice_coords(board,'x')
    else:
        board = function.choice_coords(board,'o')
    step += 1
    if function.check_board(board) is not None:
        print(f'Победа:{function.check_board(board)}')
        print()
        run = False