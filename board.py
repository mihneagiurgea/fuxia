def init_matrix(size=9, value=0):
    state = []
    for i in xrange(size):
        state.append([value] * size)
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

    def _recompute_possibilites(self):
        """Gets all possibilites for each cell in this board."""
        row_digits = init_matrix(size=10, value=1)
        column_digits = init_matrix(size=10, value=1)
        block_digits = init_matrix(size=10, value=1)
        # TODO - this break the pattern, improve it
        for i in xrange(9):
            for j in xrange(9):
                cell = self._board[i][j]
                if cell:
                    row_digits[i][cell] = 0
                    column_digits[j][cell] = 0
                    block_digits[i / 3 * 3 + j / 3][cell] = 0

        self._possibilities = {}
        for i in xrange(9):
            for j in xrange(9):
                # Skip cell that are not empty.
                if self._board[i][j]:
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
                self._possibilities[(i,j)] = temp

    def get(self, i, j):
        return self._board[i][j]

    def fill(self, i, j, value):
        """Fills a cell (empty or not) with a certain value."""
        if self._board[i][j] != 0:
            # This cell is not empty, clear it first.
            self.clear(i, j)

        self._board[i][j] = value

        # This is O(N), but acceptable for now.
        for k in xrange(9):
            if value in self._possibilities.get((i,k), []):
                self._possibilities[(i,k)].remove(value)
            if value in self._possibilities.get((k,j), []):
                self._possibilities[(k,j)].remove(value)
            # Remove value from all cells within the same block as (i,j).
            bi = i / 3 * 3 + k / 3
            bj = j / 3 * 3 + k % 3
            if value in self._possibilities.get((bi,bj), []):
                self._possibilities[(bi,bj)].remove(value)

    def clear(self, i, j):
        """Clears a filled cell."""
        if self._board[i][j] == 0:
            # This cell is already empty, nothing to clear.
            return
        self._board[i][j] = 0

        self._recompute_possibilites()

    def get_possibilities(self, i, j):
        if self._board[i][j] != 0:
            raise ValueError('Cell is not empty.')

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


