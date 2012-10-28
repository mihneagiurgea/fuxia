====================================
Project: Distributed Sudoku Generator
====================================

===========
Team: FUXIA
===========
    Andrei Grigorean
    Sonia Stan
    Mihnea Giurgea

====================
Project Description:
====================
  The Distributed Sudoku Generator Project generates Sudoku games which have different levels of difficulty. Traditionaly
the Sudoku games are divided into five categories, according to human perceived difficulty:

  - extremely easy
  - easy
  - medium
  - difficult
  - evil

  We have decided to keep the same five levels in our implementation of the generator.
__"Generating"__

Four factors affecting the difficulty level are taken into consideration in this metrics
respectively as follows:
  - the total amount of given cells,
  - the lower bound of given cells in each row and column,
  - applicable techniques by human logic thinking, and
  - enumerating search times by computer.

=======================
Project Implementation:
=======================

Solution's Building Blocks
--------------------------
There are three fundamental entities used in our implementation:
 - Solver
    - input: an incomplete Sudoku board
    - output:
      - None: there is no solution for solving the board
      - solution: if there exists at least one posssible solution, it returns the completed Sudoku board
    - explanation:
      - simple baktracking using few optimizations
 - Las Vegas
 - Digger

Project Architecture:

