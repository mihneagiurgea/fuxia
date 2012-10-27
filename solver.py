# States:
import copy

def init_matrix(value=0):
    state = []
    for i in xrange(10):
        state.append([value] * 10)
    return state

def read_board(filename):
    board = []
    with open(filename, 'r') as f:
        for line in f:
            row = [int(x) for x in line.split()]
            board.append(row)
    return board

board = init_matrix()
board[0][1] = 9
board[1][1] = 7
board[8][0] = 1
board[0][8] = 3


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
    cell_to_possibilites = get_possibilites(board)

    #TODO - this is hacky, rewrite
    if cell_to_possibilites is None:
        # We can no longer advance.
        return None

    if len(cell_to_possibilites) == 0:
        # Final board position, we have a solution.
        return board

    # This would not stand on my code review :)
    cell_to_possibilites_items = cell_to_possibilites.items()

    cell_to_possibilites_items.sort(key=lambda i: len(i[1]))

    for (i, j), possibilities in cell_to_possibilites_items:
        for digit in possibilities:
            new_board = copy.deepcopy(board)
            new_board[i][j] = digit
            partial_result = solve(new_board)
            if partial_result:
                return partial_result

    return None

def print_board(board):
    for row in board:
        print ' '.join(map(str, row))

if __name__ == '__main__':
    board = read_board('hard_board.txt')
    print 'Read board:'
    print_board(board)
    #
    # print 'Pos(0,0): %s' % get_possibilites(board)[0,0]
    solution = solve(board)
    print 'Solution:'
    print_board(solution)