# Vivaaaa, Las Vegas!

import random

from solver import init_matrix

def _is_conflicting(board, i1, j1, i2, j2):
    if board[i1][j1] != board[i2][j2]:
        return False
    if i1 == i2:
        return True
    if j1 == j2:
        return True
    # TODO - write block(i,j)
    if i1 / 3 * 3 + j1 / 3 == i2 / 3 * 3 + j2 / 3:
        return True
    return False

def _backtracking(board, givens, position):
    given = givens[position]
    while True:
        board[given[0]][given[1]] = random.randrange(10)
        for p in xrange(position):
            if _is_conflicting(board, givens[p], givens[position]):
                # Current position is not valid.






def las_vegas(givens_count=11):
    # Generate some random positions.
    all_positions = []
    for i in xrange(9):
        for j in xrange(9):
            all_positions.append((i,j))
    random.shuffle(all_positions)
    givens = all_positions[givens_count]

    board = init_matrix()

def fill_random_cell(board, i, j):
    """Fills a random cell with a random digit, avoiding conflicts."""
    while True:
