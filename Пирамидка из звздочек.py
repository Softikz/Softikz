def cube(rows):
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))

cube(11)