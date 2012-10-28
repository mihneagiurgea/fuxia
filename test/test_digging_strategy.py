import unittest2 as unittest

from digging_strategy import DiggingStrategy

class TestDiggingStrategy(unittest.TestCase):

    def test_generate_randomized_cells(self):
        test = DiggingStrategy(1)
        # Test cells in strategy:
        # have coordinates of form: (x,y)
        # with values x, y between 0 and 9
        for cell in test.cells:
            self.assertTrue(isinstance(cell, tuple))
            self.assertTrue(len(cell) == 2)
            self.assertIn(cell[0], range(0,9))
            self.assertIn(cell[1], range(0,9))
        # Test we have 81 different cells.
        self.assertTrue(len(test.cells) == 81)
        self.assertTrue( len(set(test.cells)) == len(test.cells) )
