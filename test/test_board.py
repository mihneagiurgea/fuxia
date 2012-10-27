import unittest2 as unittest

from solver import *

easy_board = read_board("easy_board.txt")

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

    def test_get_possibilities(self):
        x, y = 2, 2
        posib = get_possibilites(easy_board)
        init_len = len(posib[(x-1,y)])

        new_len =  change_cell(easy_board, x, y, x-1, y)
        self.assertLess(new_len, init_len)

        new_len = change_cell(easy_board, x, y, x, y-1)
        self.assertLess(new_len, init_len)

        new_len = change_cell(easy_board, x, y, x-1, y-1)
        self.assertLess(new_len, init_len)
