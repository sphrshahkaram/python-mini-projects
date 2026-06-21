import copy


board = [
    [None, None , None],
    [None, None , None],
    [None, None , None],
]

           

def player(board):
    X = 0
    O =0
    for i in board :
        for j in i:
            if  j == "X":
                X+=1
            elif j == "O":
                O +=1
    if X > O:
        return "O"
    elif O > X:
        return "X"
                    
    else:
        return "X"
    

def actions(board):
    khali = set()
    for i in range(3):
        for j in range(3):
            if board[i][j]== None:
                khali.add((i,j))
    return khali


def result(board, actions):
    new_board = copy.deepcopy(board)
    nobat  = player(board)
    row , col =actions
    new_board[row][col] = nobat
    return new_board



def winner(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == "X":
            return "X"
        elif board[0][0] == "O":
            return "O"
        else:
            pass
    
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] == "X":
            return "X"
        elif board[1][0] == "O":
            return "O"
        else:
            pass
        
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] == "X":
            return "X"
        elif board[2][0] == "O":
            return "O"
        else:
            pass


    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] == "X":
            return "X"
        elif board[0][0] == "O":
            return "O"
        else:
            pass
    
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1] == "X":
            return "X"
        elif board[0][1] == "O":
            return "O"
        else:
            pass
        
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2] == "X":
            return "X"
        elif board[0][2] == "O":
            return "O"
        else:
            pass

    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return "X"
        elif board[0][0] == "O":
            return "O"
        else:
            pass
    
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return "X"
        elif board[0][2] == "O":
            return "O"
        else:
            pass
        
    return None
    


def terminal(board):
    if len(actions(board)) == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False

def utility(board):
    win = winner(board)
    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0
    
def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = -10  
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v



def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = 10
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    if terminal(board):
        return None
    
    turn = player(board)
    
    if turn == "X":
        best_score = -10
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else:
        worst_score=10
        best_action =None
        for action in actions(board):
            score =max_value(result(board, action))
            if score< worst_score:
                worst_score = score
                best_action = action
        return best_action
        


print(minimax(board))
