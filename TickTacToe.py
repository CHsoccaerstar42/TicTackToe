def test_win(b):
    win = False
    tie = True
    if b[0] == b[1] == b[2] and b[0] != '':
        win = True
        player = b[0]
    if b[3] == b[4] == b[5] and b[3] != '':
        win = True
        player = b[3]
    if b[6] == b[7] == b[8] and b[6] != '':
        win = True
        player = b[6]
    if b[0] == b[3] == b[6] and b[0] != '':
        win = True
        player = b[0]
    if b[1] == b[4] == b[7] and b[1] != '':
        win = True
        player = b[1]
    if b[2] == b[5] == b[8] and b[2] != '':
        win = True
        player = b[2]
    if b[0] == b[4] == b[8] and b[0] != '':
        win = True
        player = b[0]
    if b[2] == b[4] == b[6] and b[2] != '':
        win = True
        player = b[2]
    for index in b:
        if index == '':
            tie = False
    return(win, tie)

def print_board(board):
    for count in range(len(board)):
        print('[', board[count], ']', end='\t')
        if (count + 1) % 3 == 0:
            print('\n')
    return()

playAgain = True

while playAgain:

    board = ['', '', '',
             '', '', '',
             '', '', '']
    run = True


    while run:
        print_board(board)
        loop = True
        while loop:
            pos_f = 0
            pos = input('Player 1 enter coordinates:')
            p1x = int(pos[1])
            p1y = int(pos[3])
            if p1x > 0:
                for count in range(p1y - 1):
                    pos_f += 3
                pos_f += (p1x - 1)
                try:
                    if board[pos_f] == '':
                       loop = False
                    else:
                        print('Position is already taken')
                except:
                    print('Out of range')
            else:
                print('Out of range')
        board[pos_f] = 'X'
        win, tie = test_win(board)
        if win:
            run = False
            print_board(board)
            print('Player 1 Wins!')
        elif tie:
            run = False
            print('Tie')
        else:
            print_board(board)
            loop = True
            while loop:
                pos_f = 0
                pos = input('Player 2 enter coordinates:')
                p2x = int(pos[1])
                p2y = int(pos[3])
                if p2x > 0:
                    for count in range(p2y - 1):
                        pos_f += 3
                    pos_f += (p2x - 1)
                    try:
                        if board[pos_f] == '':
                           loop = False
                        else:
                            print('Position is already taken')
                    except:
                        print('Out of range')
                else:
                    print('Out of range')
            board[pos_f] = 'O'
            win, tie = test_win(board)
            if win:
                run = False
                print_board(board)
                print('Player 2 Wins!')
    ui = input('Play again? (y/n): ')
    if ui == 'n':
        playAgain = False
