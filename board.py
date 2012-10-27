def init_matrix(value=0):
    state = []
    for i in xrange(9):
        state.append([value] * 9)
    return state

def get_block(i, j):
    return i / 3 * 3 + j / 3

class Board(object):

    @classmethod
    def from_file(cls, filename):
        """Load a board from a filename."""
        matrix = []
        with open(filename, 'r') as f:
            for line in f:
                row = [int(x) for x in line.split()]
                matrix.append(row)
        # Initialize an empty board, use fill to add all read values.
        board = Board()
        for i in xrange(9):
            for j in xrange(9):
                board.fill(i, j, matrix[i][j])
        return board

    def __init__(self):
        """Initializes an empty Board."""
        self._board = init_matrix()
        # Initialize _possibilities: for each empty cell, store a list of all
        # possible values that can be filled there.
        self._possibilities = {}
        for i in xrange(9):
            for j in xrange(9):
                self._possibilities[(i,j)] = range(1, 10)

    def get(self, i, j):
        return self._board[i][j]

    def fill(self, i, j, value):
        """Fills in an empty cell with value."""
        if self._board[i][j] != 0:
            raise ValueError('Call is not empty.')

        self._board[i][j] = value

        # This is O(N), but acceptable for now.
        for k in xrange(9):
            if value in self._possibilities[(i,k)]:
                self._possibilities[(i,k)].remove(value)
            if value in self._possibilities[(k,j)]:
                self._possibilities[(k,j)].remove(value)
            # Remove value from all cells within the same block as (i,j).
            bi = i / 3 * 3 + k / 3
            bj = j / 3 * 3 + k % 3
            if value in self._possibilities[(bi,bj)]:
                self._possibilities[(bi,bj)].remove(value)

    def get_possibilities(self, i, j):
        if self._board[i][j] != 0:
            raise ValueError('Call is not empty.')

        if self._possibilities[(i,j)]:
            return self._possibilities[(i,j)]
        else:
            # This cell cannot be filled in with any values.
            return None

    def __repr__(self):
        string = ''
        for row in self._board:
            row_string = ' '.join(map(str, row))
            string += '%s\n' % row_string
        return string

    def _is_conflicting(self, i1, j1, i2, j2):
        """Checks if two non-empty cells on the same row, column or block have
        the same value."""
        if self._board[i1][j1] == 0 or self._board[i2][j2]:
            return False
        if self._board[i1][j1] != self._board[i2][j2]:
            return False
        if i1 == i2:
            return True
        if j1 == j2:
            return True
        if get_block(i1, j1) == get_block(i2, j2):
            return True
        return False

    def is_valid(self):
        """Checks if the board is a correct sudoku configuration.

        The board can be incomplete - contains empty cells.
        """
        for i1 in xrange(9):
            for j1 in xrange(9):
                for i2 in xrange(9):
                    for j2 in xrange(9):
                        if (i1, j1) == (i2, j2):
                            continue
                        if self._is_conflicting(i1, j1, i2, j2):
                            return False
        return True


