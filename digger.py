import random

from board import Board
from solver import solve
from digging_strategy import DiggingStrategy

def dig_cells(board, digging_strategy):
    dig_count = 0
    for (i, j) in digging_strategy.cells:
        prev_value = board.get(i, j)
        if prev_value == 0:
            # Skip empty cells, nothing to dig.
            continue
        board.clear(i, j)

        possibilities = board.get_possibilities(i, j)
        possibilities.remove(prev_value)

        has_another_solution = False
        for new_value in possibilities:
            # Check if there is a solution with new_value in cell (i, j)
            board.fill(i, j, new_value)
            # comments?
            # print 'Trying to solve | diggs = %d\n%r' % (dig_count, board)
            if solve(board):
                has_another_solution = True
                break

        # If we found another solution by filling this cell with a value
        # different than new_value, than we cannot dig this cell (it would
        # yield a board with multiple solutions).
        if has_another_solution:
            # Discard changes.
            board.fill(i, j, prev_value)
        else:
            # This cell is a correct dig, leave it like this.
            dig_count += 1

        if dig_count >= digging_strategy.limit:
            return board
    return board

if __name__ == '__main__':
    board = Board.from_file('easy_board.txt')
    digging_strategy = DiggingStrategy(1)
    partial_board = dig_cells(board, digging_strategy)
    print 'Partial board:\n%r' % partial_board