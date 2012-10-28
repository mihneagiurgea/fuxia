import random

class DiggingStrategy(object):
    """TODO - write me"""

    def __init__(self, difficulty):
        if not isinstance(difficulty, int):
            raise ValueError('invalid difficulty argument: expected int')
        if difficulty == 1:
            self.generate_randomized_cells()
            self.max_empty_cells = 4
            self.limit = 31
        elif difficulty == 2:
            self.generate_randomized_cells()
            self.max_empty_cells = 5
            self.limit = 45
        elif difficulty == 3:
            self.generate_jumping_once_cell()
            self.max_empty_cells = 6
            self.limit = 49
        elif difficulty == 4:
            self.generate_wandering_along_s()
            self.max_empty_cells = 7
            self.limit = 53
        elif difficulty == 5:
            self.generate_ordered_cells()
            self.max_empty_cells = 9
            self.limit = 59
        else:
            raise ValueError('invalid difficulty level: %d' % difficulty)

    def can_dig(self, board, i, j):
        nr_empty_cells = 0
        for k in xrange(9):
            if board.get(i, k) == 0:
                nr_empty_cells += 1
        if nr_empty_cells >= self.max_empty_cells:
            return False

        nr_empty_cells = 0
        for k in xrange(9):
            if board.get(k, j) == 0:
                nr_empty_cells += 1
        if nr_empty_cells >= self.max_empty_cells:
            return False

        return True

    def generate_ordered_cells(self):
        self.cells = []
        for i in xrange(9):
            for j in xrange(9):
                self.cells.append((i,j))

    def generate_randomized_cells(self):
        self.generate_ordered_cells()
        random.shuffle(self.cells)

    def generate_wandering_along_s(self):
        self.cells = []
        for i in xrange(9):
            for j in xrange(9):
                if i % 2 == 0:
                    cell = (i, j)
                else:
                    cell = (i, 8-j)
                self.cells.append(cell)

    def generate_jumping_once_cell(self):
        self.generate_wandering_along_s()
        temp = []
        for i in xrange(0, len(self.cells), 2):
            temp.append(self.cells[i])
        for i in xrange(1, len(self.cells), 2):
            temp.append(self.cells[i])
        self.cells = temp