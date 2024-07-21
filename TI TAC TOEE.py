# -*- coding: utf-8 -*-
"""Untitled39.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nw_ZW81nvyVoGkfa1Alb4zdLc3i2GXVQ
"""

def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return 10 if board[i][0] == 'X' else -10
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return 10 if board[0][i] == 'X' else -10
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return 10 if board[0][2] == 'X' else -10
    return 0

def is_moves_left(board):
    return any('_' in row for row in board)

def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = '_'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = '_'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = '_'
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def nextMove(player, board):
    if player == 'O':
        # If we're playing as O, we need to flip X and O in the board
        board = [['O' if cell == 'X' else 'X' if cell == 'O' else '_' for cell in row] for row in board]

    best_move = find_best_move(board)
    print(f"{best_move[0]} {best_move[1]}")

# Read input
player = input().strip()
board = [list(input().strip()) for _ in range(3)]

# Call the nextMove function
nextMove(player, board)