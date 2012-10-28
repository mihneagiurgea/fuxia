import sys
import cloud

from digging_strategy import DiggingStrategy
from digger import Digger
from las_vegas import generate_terminal_pattern

def generate_sudoku_with_unique_solution(difficulty):
    """Generates a partially completed sudoku with a unique solution, of the
    given difficulty (1 through 5)."""
    # Generate a terminal pattern (fully completed sudoku)
    terminal_pattern = generate_terminal_pattern()
    # Instantiate a Digger instance for the selected difficulty.
    digging_strategy = DiggingStrategy(difficulty)
    digger = Digger(digging_strategy)

    sudoku = digger.dig_cells(terminal_pattern)
    return sudoku

if __name__ == '__main__':
    difficulty = int(sys.argv[1])

    # cloud.start_simulator()
    # sudoku = generate_sudoku_with_unique_solution(difficulty)
    jid = cloud.call(generate_sudoku_with_unique_solution, difficulty)
    sudoku = cloud.result(jid)
    print 'Generated sudoku with unique solution:\n%r' % sudoku
