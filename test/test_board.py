import unittest2 as unittest

from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board.from_file('test/fixtures/easy_board.txt')

    def assertPossibilities(self, board, i, j, expected_possibilities):
        possibilities = board.get_possibilities(i, j)
        self.assertEqual(set(possibilities), set(expected_possibilities))

    def test_from_file(self):
        """Check the reading from file was correct."""
        self.assertIsNotNone(self.board)
        self.assertEqual(self.board.get(0, 1), 0)
        self.assertEqual(self.board.get(0, 2), 7)

    def test_is_valid(self):
        """Check that a given board has a valid configuration."""
        self.assertIsNotNone(self.board)
        self.assertTrue(self.board.is_valid())

    def test_get_possibilities(self):

        self.assertEqual(set(self.board.get_possibilities(0, 0)), set([2, 3, 9]))

        self.assertEqual(set(self.board.get_possibilities(2, 1)), set([4, 8]))

        self.board.fill(0, 1, 2)
        self.assertEqual(set(self.board.get_possibilities(0, 0)), set([3, 9]))

        self.board.fill(1, 1, 3)
        self.assertEqual(self.board.get_possibilities(0, 0), [9])

        # Try to fill in a cell that is not empty.
        self.board.fill(1, 1, 4)
        self.assertEqual(set(self.board.get_possibilities(0, 0)), set([3, 9]))

        self.board.fill(8, 0, 9)
        self.assertEqual(self.board.get_possibilities(0, 0), [3])

        self.board.fill(7, 0, 3)
        self.assertEqual(self.board.get_possibilities(0, 0), None)

        # Ensure we can't get possibilities of a not empty cell.
        with self.assertRaises(ValueError):
            self.board.get_possibilities(8, 0)

    def test_clear(self):
        # Test that clearing a cell will increase the possibilities of
        # cells of the same column / row / block.
        self.assertPossibilities(self.board, 0, 0, [2, 3, 9])

        self.board.clear(0, 2)
        self.assertPossibilities(self.board, 0, 0, [2, 3, 7, 9])

        self.board.clear(6, 0)
        self.assertPossibilities(self.board, 0, 0, [2, 3, 4, 7, 9])

        self.assertPossibilities(self.board, 2, 6, [4, 7, 8, 9])
        self.board.clear(1, 7)
        self.assertPossibilities(self.board, 2, 6, [4, 7, 8, 9])

    def test_clear_on_filled_board(self):
        board = Board.from_file('test/fixtures/filled_board.txt')

        board.clear(0, 0)
        board.clear(0, 1)
        self.assertPossibilities(board, 0, 1, [6])
