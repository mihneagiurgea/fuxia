# Vivaaaa, Las Vegas!

import random

from board import Board

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
    if position >= len(givens):
        # We've manage to fill all the given positions, we can stop.
        return board

    # Try to fill in cell for the current given.
    i, j = givens[position]

    # Compute all posibilities for this cell and shuffle them.
    possibilities = board.get_possibilities(i, j)
    random.shuffle(possibilities)
    # Try to fill in this cell, and if that value does not yield a solution,
    # switch to the next one.
    for value in possibilities:
        board.fill(i, j, value)
        solution = _backtracking(board, givens, position+1)
        if solution:
            return solution
    # No possible solutions were found (for the current givens).
    # Take a step back in the recursion, and try another value.
    return None

def las_vegas(givens_count=11):
    # Generate some random positions.
    all_positions = []
    for i in xrange(9):
        for j in xrange(9):
            all_positions.append((i,j))
    givens = random.sample(all_positions, givens_count)

    board = Board()
    board = _backtracking(board, givens, 0)
    print board

if __name__ == '__main__':
    las_vegas()