"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

x = [[EMPTY, EMPTY, EMPTY],
     [EMPTY, EMPTY, EMPTY],
     [EMPTY, EMPTY, EMPTY]]


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
    # Counter for X on the board
    cX = 0

    # Counter for O on the board
    cO = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                cX += 1
            elif board[i][j] == O:
                cO += 1

    if cX > cO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pactions = set()

    # Possible actions are any field that is EMPTY
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                pactions.add((i, j))
    return pactions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board_state = copy.deepcopy(board)
    # Board + action = new board state

    new_board_state[action[0]][action[1]] = player(board)

    return new_board_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Check if there are three same parameters vertical, diagonal or horizontal
    Check if they are not empty
    Check which player is the winner
    """
    # Check if there is a winner in a row
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not EMPTY:
            if board[row][0] == X:
                return X
            else:
                return O

    # Check if there is a winner in a column
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            if board[0][col] == X:
                return X
            else:
                return O

    # Check if there is a diagonal winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        if board[0][0] == X:
            return X
        else:
            return O
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        if board[0][2] == X:
            return X
        else:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:

            # max_value returns two values because of alpha-beta pruning
            value, move = max_value(board)

            # Only move gets returned here because value is only needed inside of max_value and min_value function
            return move

        else:
            value, move = min_value(board)
            return move


# Part of minimax that aims to maximize the value

def max_value(board):

    # Check if there is a winner
    if terminal(board):
        return utility(board), None

    v = -math.inf
    move = None

    # Go through all possible actions
    for action in actions(board):

        # See which turn is best based on the next turn of opponent
        tmp_value, act = min_value(result(board, action))
        if tmp_value > v:
            v = tmp_value
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = math.inf
    move = None

    # Go through all possible actions
    for action in actions(board):

        # See which turn is best based on the next turn of opponent
        tmp_value, act = max_value(result(board, action))
        if tmp_value < v:
            v = tmp_value
            move = action
            if v == -1:
                return v, move
    return v, move
