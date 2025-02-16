"""
File name: warnsdorffs_rule.py
Author: Troy Chin, Jacob Hellebrand, Anderson Pham, Cristian Verduzco, Christian Barajas
Date: 2025 Feb 15
Description: This script implements Warnsdorff's rule for solving the knight's tour problem.
Version: 1.0
"""

import random

def is_valid_move(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def get_onward_moves(x, y, board, N, moves):
    count = 0
    for dx, dy in moves:
        if is_valid_move(x + dx, y + dy, board, N):
            count += 1
    return count

def warnsdorff_knights_tour(N):
    # Initialize board with -1 (unvisited)
    board = [[-1 for _ in range(N)] for _ in range(N)]
    
    # Knight's possible moves
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    # Start at a random position
    start_x, start_y = random.randint(0, N - 1), random.randint(0, N - 1)
    board[start_x][start_y] = 0
    
    x, y = start_x, start_y
    
    for step in range(1, N * N):
        # Find valid moves
        possible_moves = []
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y, board, N):
                degree = get_onward_moves(new_x, new_y, board, N, moves)
                possible_moves.append((degree, new_x, new_y))
        
        # No available moves, fail
        if not possible_moves:
            return None
        
        # Choose move with minimum onward degree (Warnsdorff’s heuristic)
        possible_moves.sort()
        _, x, y = possible_moves[0]
        board[x][y] = step
    
    return board

def print_board(board, N):
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))
    print()

# Example usage
N = 8  # Board size
solution = warnsdorff_knights_tour(N)
if solution:
    print("Knight's Tour Solution:")
    print_board(solution, N)
else:
    print("No tour found.")


    

