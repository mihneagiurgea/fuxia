# States:
import copy

from board import Board

def solve(board):
    """Tries to solve a board instance, returning the first solution found.
    Returns None when no solution exists."""
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
    for digit in possibilities:
        new_board = copy.deepcopy(board)
        new_board.fill(mini, minj, digit)
        partial_result = solve(new_board)
        if partial_result:
           return partial_result

    return None

if __name__ == '__main__':
    board = Board.from_file('test/fixtures/insane_board.txt')
    print 'Read board:\n%r' % board

    solution = solve(board)
    print 'Solution:\n%r' % solution
