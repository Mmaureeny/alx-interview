#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

def print_solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print(j, end=' ')
        print()
    print()

def is_safe(board, row, col):
"""Check if there is a queen in the same column
"""
    for i in range(row):
        if board[i][col] == 1:
            return False

"""Check upper left diagonal
"""
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

"""Check upper right diagonal
"""
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row):
    if row == len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1)
            board[row][col] = 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for x in range(N)] for y in range(N)]
    solve_n_queens(board, 0)
