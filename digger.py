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

from board import Board
from solver import solve
from digging_strategy import DiggingStrategy

class Digger(object):

    def __init__(self, digging_strategy):
        self.digging_strategy = digging_strategy

    def dig_cells(self, terminal_pattern):
        board = copy.deepcopy(terminal_pattern)
        dig_count = 0
        for (i, j) in self.digging_strategy.cells:
            if not self.digging_strategy.can_dig(board, i, j):
                continue

            prev_value = board.get(i, j)
            board.clear(i, j)

            possibilities = board.get_possibilities(i, j)
            possibilities.remove(prev_value)

            has_another_solution = False
            for new_value in possibilities:
                # Check if there is a solution with new_value in cell (i, j)
                board.fill(i, j, new_value)
                # comments?
                if solve(board):
                    has_another_solution = True
                    break

            # If we found another solution by filling this cell with a value
            # different than new_value, than we cannot dig this cell (it would
            # yield a board with multiple solutions).
            if has_another_solution:
                # print 'Has solution: (%d, %d)' % (i, j)
                # Discard changes.
                board.fill(i, j, prev_value)
            else:
                # print 'Dug out: (%d, %d)' % (i, j)
                # This cell is a correct dig, leave it like this.
                board.clear(i, j)
                dig_count += 1

            if dig_count >= self.digging_strategy.limit:
                return board
        return board
