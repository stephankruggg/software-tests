import unittest

from src.puzzle_game import PuzzleGame
from src.invalid_position_exception import InvalidPositionException
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To12345X786

# Branch Coverage
# Branches
# A) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (T) - 7 (T) - 8
# B) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (T) - 7 (F) - 10
# C) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (F) - 10
# D) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (F) - 9
# E) 1 - 2 (T) - 3 (T) - 4 (F) - 9
# F) 1 - 2 (T) - 3 (F) - 9
# G) 1 - 2 (F) - 9

class TestBranchCoverage(unittest.TestCase):
    def setUp(self) -> None:
        self._puzzle_game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(self._puzzle_game)

    def test_returns_empty_when_calling_get_tile_with_line_and_column_of_empty_position(self):
        # A) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (T) - 7 (T) - 8
        self.assertEqual(
            " ",
            self._puzzle_game.get_tile(2, 3)
        )

    def test_returns_tile_when_calling_get_tile_with_line_of_empty_position_but_different_valid_column(self):
        # B) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (T) - 7 (F) - 10
        self.assertEqual(
            5,
            self._puzzle_game.get_tile(2, 2)
        )

    def test_returns_tile_when_calling_get_tile_with_valid_line_different_than_line_of_empty_position(self):
        # C) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (T) - 6 (F) - 10
        self.assertEqual(
            3,
            self._puzzle_game.get_tile(1, 3)
        )

    def test_raises_invalid_position_when_calling_get_tile_with_column_above_board_number_of_columns(self):
        # D) 1 - 2 (T) - 3 (T) - 4 (T) - 5 (F) - 9
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(1, 4)

    def test_raises_invalid_position_when_calling_get_tile_with_negative_column(self):
        # E) 1 - 2 (T) - 3 (T) - 4 (F) - 9
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(1, -1)

    def test_raises_invalid_position_when_calling_get_tile_with_line_above_board_number_of_lines(self):
        # F) 1 - 2 (T) - 3 (F) - 9
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(4, 1)

    def test_raises_invalid_position_when_calling_get_tile_with_negative_line(self):
        # G) 1 - 2 (F) - 9
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(-1, 1)
