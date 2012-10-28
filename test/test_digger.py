import unittest
import cloud

from digger import Digger
from digging_strategy import DiggingStrategy
from las_vegas import generate_terminal_pattern
from solver import solve

# Initiate the picloud simulator (localhost only) to speed up tests.
cloud.start_simulator()

class TestDigger(unittest.TestCase):

    def setUp(self):
        digging_strategy = DiggingStrategy(1)
        self.digger = Digger(digging_strategy)
        self.terminal_pattern = generate_terminal_pattern()

    def test_dig_cells_finds_a_valid_solution(self):
        partial_board = self.digger.dig_cells(self.terminal_pattern)
        self.assertIsNotNone(partial_board)
        self.assertTrue(partial_board.is_valid())

    def test_dig_cells_finds_a_unique_solution(self):
        partial_board = self.digger.dig_cells(self.terminal_pattern)
        self.assertIsNotNone(partial_board)
        # For each empty cell in partial_board, try to fill it with a value
        # different than the one from terminal_pattern. No solutions should
        # yield from this. If any do, then this is not a unique solution.
        for i in xrange(9):
            for j in xrange(9):
                if partial_board.get(i, j) != 0:
                    # Not an empty cell, move on.
                    continue

                possibilities = partial_board.get_possibilities(i, j)
                possibilities.remove(self.terminal_pattern.get(i, j))
                for value in possibilities:
                    partial_board.fill(i, j, value)
                    self.assertIsNone(solve(partial_board))

                # Discard changes.
                partial_board.clear(i, j)

