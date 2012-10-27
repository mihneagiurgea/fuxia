# States:
import copy

from board import Board

def solve(board):
    mini, minj, minlen = 10, 10, 10
    for i in xrange(9):
        for j in xrange(9):
            if board.get(i, j) != 0:
                # This cell is already filled, move on.
                continue

            possibilities = board.get_possibilities(i, j)
            if possibilities is None:
                # We can no longer advance, no solution from this state.
                return None
            if len(possibilities) < minlen:
                mini, minj, minlen = i, j, len(possibilities)

    if minlen == 10:
        # No empty cells found, we found a solution.
        return board

    # Use only the first.
    for digit in board.get_possibilities(mini, minj):
        new_board = copy.deepcopy(board)
        # print 'fill(%s, %s, %s)' % (mini, minj, digit)
        new_board.fill(mini, minj, digit)
        partial_result = solve(new_board)
        if partial_result:
           return partial_result

    return None

if __name__ == '__main__':
    board = Board.from_file('insane_board.txt')
    print 'Read board:\n%r' % board

    solution = solve(board)
    print 'Solution:\n%r' % solution
