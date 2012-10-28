import random

class DiggingStrategy(object):
    """TODO - write me"""

    def __init__(self, difficulty):
        if not isinstance(difficulty, int):
            raise ValueError('invalid difficulty argument: expected int')
        if difficulty in (1, 2):
            self.generate_randomized_cells()
        elif difficulty == 3:
            self.generate_jumping_once_cell()
        elif difficulty == 4:
            self.generate_wandering_along_s()
        elif difficulty == 5:
            self.generate_ordered_cells()
        else:
            raise ValueError('invalid difficulty level: %d' % difficulty)

        self.limit = 50

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