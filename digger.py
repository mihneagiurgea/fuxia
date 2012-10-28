import random
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

if __name__ == '__main__':
    from las_vegas import generate_terminal_pattern

    terminal_pattern = generate_terminal_pattern()
    digging_strategy = DiggingStrategy(5)
    partial_board = dig_cells(terminal_pattern, digging_strategy)
    print 'Partial board:\n%r' % partial_board