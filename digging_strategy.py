import random

class DiggingStrategy(object):

    def __init__(self, difficulty):
        self.generate_randomized_cells()
        self.limit = 10

    def generate_randomized_cells(self):
        self.cells = []
        for i in xrange(9):
            for j in xrange(9):
                self.cells.append((i,j))
        random.shuffle(self.cells)
