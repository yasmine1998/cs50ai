"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if all(i == [EMPTY, EMPTY, EMPTY] for i in board):
        return X
        
    if terminal(board):
        return "game is over"
      
    cx = 0
    co = 0
    for l in board:
        cx += l.count(X)
        co += l.count(O)
        
    if cx > co:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()
    
    if terminal(board):
        return "game is over"
        
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                act.add((i,j))
    return act

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (action[0], action[1]) in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2),(1,0),(2,0),(2,1)] and board[action[0]][action[1]] != EMPTY:
        raise NameError('Action not valid')
        
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    cond_ind = [[(0, 0), (0, 1), (0, 2)],[(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (1, 1), (2, 1)]]
    conditions = [board[0][0] == board[0][1] == board[0][2], board[2][0] == board[2][1] == board[2][2], board[0][0] == board[1][0] == board[2][0], board[0][2] == board[1][2] == board[2][2], board[0][0] == board[1][1] == board[2][2], board[0][2] == board[1][1] == board[2][0], board[1][0] == board[1][1] == board[1][2], board[0][1] == board[1][1] == board[2][1]]
    
    if any(conditions):
        action = cond_ind[conditions.index(True)][0]
        return board[action[0]][action[1]]
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None and any(EMPTY in sublist for sublist in board):
        return False
    else:
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
        
    elif winner(board) == O:
        return -1
        
    else:
        return 0

def MaxVal(board, depth):
    if terminal(board):
        return utility(board), []
        
    v = -math.inf
    list_v = []
    
    for action in actions(board):
        m = max(v, MinVal(result(board, action), 1)[0])
        if depth == 1:
            v = m
        else:
            list_v.append(m)
            
    return (v,list_v)
    
def MinVal(board, depth):
    if terminal(board):
        return utility(board), []
        
    v = math.inf
    list_v = []
   
    for action in actions(board):
        m = min(v, MaxVal(result(board, action), 1)[0])
        if depth == 1:
            v = m
        else:
            list_v.append(m)
        
    return (v,list_v)
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    depth = 0
    if player(board) == X:
        v, list_v = MaxVal(board, depth)
        return list(actions(board))[list_v.index(max(list_v))]
        
    else:
        v, list_v = MinVal(board, depth)
        return list(actions(board))[list_v.index(min(list_v))]
        
