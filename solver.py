# States:
import copy

from board import Board

def get_possibilites(board):
    """Gets all possibilites for each cell in this board."""
    row_digits = init_matrix(1)
    column_digits = init_matrix(1)
    block_digits = init_matrix(1)
    # TODO - this break the pattern, improve it
    for i in xrange(9):
        for j in xrange(9):
            cell = board[i][j]
            if cell:
                row_digits[i][cell] = 0
                column_digits[j][cell] = 0
                block_digits[i / 3 * 3 + j / 3][cell] = 0

    result = {}
    for i in xrange(9):
        for j in xrange(9):
            # Is this cell free/empty?
            if board[i][j]:
                continue

            possibilites = [1] * 10
            for k in xrange(1, 10):
                if not row_digits[i][k]:
                    possibilites[k] = 0
                if not column_digits[j][k]:
                    possibilites[k] = 0
                if not block_digits[i / 3 * 3 + j / 3][k]:
                    possibilites[k] = 0
            temp = []
            for x in xrange(1, 10):
                if possibilites[x]:
                    temp.append(x)
            # No valid choises for this cell.
            if not temp:
                return None
            result[(i,j)] = temp
    return result

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


    # cell_to_possibilites = get_possibilites(board)
    #
    # #TODO - this is hacky, rewrite
    # if cell_to_possibilites is None:
    #     # We can no longer advance.
    #     return None
    #
    # if len(cell_to_possibilites) == 0:
    #     # Final board position, we have a solution.
    #     return board
    #
    # mini, minj, minlen = 10, 10, 10
    # for (i, j), possibilities in cell_to_possibilites.iteritems():
    #     if len(possibilities) < minlen:
    #         mini, minj, minlen = i, j, len(possibilities)
    #
    # # Use only the first.
    # for digit in cell_to_possibilites[(mini,minj)]:
    #     new_board = copy.deepcopy(board)
    #     new_board[mini][minj] = digit
    #     partial_result = solve(new_board)
    #     if partial_result:
    #        return partial_result
    #
    # return None

if __name__ == '__main__':
    board = Board.from_file('insane_board.txt')
    print 'Read board:\n%r' % board

    solution = solve(board)
    print 'Solution:\n%r' % solution
