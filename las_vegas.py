# Copyright (c) 2012 Andrei Grigorean, Mihnea Giurgea, Sonia Stan, MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Vivaaaa, Las Vegas!

import random

from board import Board
from solver import solve

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

    partial_board = Board()
    partial_board = _backtracking(partial_board, givens, 0)
    solution = solve(partial_board)
    return solution

def generate_terminal_pattern():
    """Generates a terminal pattern (a fully completed & valid Board)."""
    while True:
        terminal_pattern = las_vegas(givens_count=11)
        if terminal_pattern:
            return terminal_pattern
