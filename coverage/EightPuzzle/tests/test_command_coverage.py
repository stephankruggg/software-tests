import unittest

from src.puzzle_game import PuzzleGame
from src.invalid_position_exception import InvalidPositionException
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To12345X786

# Command Coverage
# Paths:
# A) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (T) - 7 (T) - 8
# B) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (F) - 10
# C) 1 - 2 (F) - 9

class TestCommandCoverage(unittest.TestCase):
    def setUp(self) -> None:
        self._puzzle_game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(self._puzzle_game)

    def test_returns_empty_when_calling_get_tile_with_line_and_column_of_empty_position(self):
        # A) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (T) - 7 (T) - 8
        self.assertEqual(
            " ",
            self._puzzle_game.get_tile(2, 3)
        )

    def test_returns_board_tile_when_calling_get_tile_with_line_different_than_line_of_empty_position(self):
        # B) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (F) - 10
        self.assertEqual(
            3,
            self._puzzle_game.get_tile(1, 3)
        )

    def test_raises_invalid_position_exception_when_line_below_0(self):
        # C) 1 - 2 (F) - 9
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(-1, 3)
