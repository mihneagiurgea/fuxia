import unittest2 as unittest

from las_vegas import las_vegas

class TestLasVegas(unittest.TestCase):
    """Testing the Las Vegas algorithm, the returned board must be a valid
    final configuration."""

    def test_las_vegas(self):
        board = las_vegas()

        # Test the generated board is valid.
        self.assertIsNotNone(board)
        self.assertTrue(board.is_valid())

        # Test board doesn't have any empty cells.
        for i in xrange(0,9):
            for j in xrange(0,9):
                self.assertTrue(board._board[i][j] != 0)
