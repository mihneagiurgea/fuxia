import unittest2 as unittest

from board import Board

class TestBoard(unittest.TestCase):

    def test_from_file(self):
        """Check the reading from file was correct."""
        board = Board.from_file('easy_board.txt')
        self.assertIsNotNone(board)
        self.assertEqual(board.get(0, 1), 0)
        self.assertEqual(board.get(0, 2), 7)

    def test_is_valid(self):
        """Check that a given board has a valid configuration."""
        board = Board.from_file('easy_board.txt')
        self.assertIsNotNone(board)
        self.assertTrue(board.is_valid())

    def test_get_possibilities(self):
        board = Board.from_file('easy_board.txt')

        self.assertEqual(set(board.get_possibilities(0, 0)), set([2, 3, 9]))

        self.assertEqual(set(board.get_possibilities(2, 1)), set([4, 8]))

        board.fill(0, 1, 2)
        self.assertEqual(set(board.get_possibilities(0, 0)), set([3, 9]))

        board.fill(1, 1, 3)
        self.assertEqual(board.get_possibilities(0, 0), [9])

        # Try to fill in a cell that is not empty.
        board.fill(1, 1, 4)
        self.assertEqual(set(board.get_possibilities(0, 0)), set([3, 9]))

        board.fill(8, 0, 9)
        self.assertEqual(board.get_possibilities(0, 0), None)

        # Ensure we can't get possibilities of a not empty cell.
        with self.assertRaises(ValueError):
            board.get_possibilities(8, 0)

    def test_clear(self):
        # Test that clearing a cell will increase the possibilities of
        # cells of the same column / row / block.
        board = Board.from_file('easy_board.txt')

        self.assertEqual(set(board.get_possibilities(0, 0)), set([2, 3, 9]))

        board.clear(0, 2)
        self.assertEqual(set(board.get_possibilities(0, 0)), set([2, 3, 7, 9]))

        board.clear(6, 0)
        self.assertEqual(set(board.get_possibilities(0, 0)), set([2, 3, 4, 7, 9]))

        self.assertEqual(set(board.get_possibilities(2, 6)), set([4, 7, 8, 9]))
        board.clear(1, 7)
        self.assertEqual(set(board.get_possibilities(2, 6)), set([3, 4, 7, 8, 9]))
