import unittest2 as unittest

from board import Board

def change_cell(board, x, y, _x, _y):
    if board[_x][_y] == 0:
        posib = get_possibilites(board)
        init_value = len(posib[(_x, _y)])

        board[x][y] = posib[(_x, _y)][0]
        posib = get_possibilites(board)

        return len(posib[_x, _y])
    else:
        raise ValueError('Cell not empty (%d, %d) = %d' % (_x, _y, board[_x][_y]))

class TestBoard(unittest.TestCase):

    def test_from_file(self):
        board = Board.from_file('easy_board.txt')
        self.assertIsNotNone(board)
        self.assertEqual(board.get(0, 1), 0)
        self.assertEqual(board.get(0, 2), 7)

    def test_get_possibilities(self):
        board = Board.from_file('easy_board.txt')

        self.assertEqual(board.get_possibilities(0, 0), [2, 3, 9])

        board.fill(0, 1, 2)
        self.assertEqual(board.get_possibilities(0, 0), [3, 9])

        board.fill(1, 1, 3)
        self.assertEqual(board.get_possibilities(0, 0), [9])

        board.fill(8, 0, 9)
        self.assertEqual(board.get_possibilities(0, 0), None)

        # Ensure we can't get possibilities of a not empty cell.
        with self.assertRaises(ValueError):
            board.get_possibilities(8, 0)