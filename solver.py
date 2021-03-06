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

import copy
import cloud

# In order to reduce overhead, only perform cloud-forks once every X solve
# function calls, instead of once every call.
MAX_LOCALHOST_DEPTH = 30

def solve(board, depth=0):
    """Tries to solve a board instance, returning the first solution found.
    Returns None when no solution exists.

    Current implementation uses picloud to parallelize the recursive calls
    of this function. However, in order to reduce overhead, instead of
    making each recursive call a remote procedure call, only do that
    once every few levels of recursion. The effect of this is that each
    job will process several levels from the recursion tree.
    """
    # Find the empty cell with the minimum number of filling possibilities.
    mini, minj, minlen = 10, 10, 10
    for i in xrange(9):
        for j in xrange(9):
            if board.get(i, j) != 0:
                # This cell is already filled, move on.
                continue

            possibilities = board.get_possibilities(i, j)
            if not possibilities:
                # We can no longer advance, no solution from this state.
                return None
            if len(possibilities) < minlen:
                mini, minj, minlen = i, j, len(possibilities)

    if minlen == 10:
        # No empty cells found, we found a solution.
        return board

    # Fill in the selected cell with each possible digit,
    # until we find a solution.
    possibilities = board.get_possibilities(mini, minj)
    if len(possibilities) == 0:
        return None
    elif len(possibilities) == 1 or depth < MAX_LOCALHOST_DEPTH:
        return branch_out_on_local(board, mini, minj, possibilities, depth+1)
    else:
        return branch_out_in_cloud(board, mini, minj, possibilities, 0)

def branch_out_in_cloud(board, i, j, possibilities, depth):
    jids = []
    for digit in possibilities:
        new_board = copy.deepcopy(board)
        new_board.fill(i, j, digit)
        jid = cloud.call(solve, new_board, depth)
        jids.append(jid)
    for result in cloud.iresult(jids):
        if result:
            return result
    return None

def branch_out_on_local(board, i, j, possibilities, depth):
    for digit in possibilities:
        new_board = copy.deepcopy(board)
        new_board.fill(i, j, digit)
        partial_result = solve(new_board, depth)
        if partial_result:
           return partial_result

    return None
