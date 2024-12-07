import unittest

from src.puzzle_game import PuzzleGame
from src.invalid_position_exception import InvalidPositionException
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To12345X786


class TestBranchCoverage(unittest.TestCase):
    def setUp(self) -> None:
        self._puzzle_game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(self._puzzle_game)

    def test_returns_tile_when_calling_get_tile_with_line_of_empty_position_but_different_valid_column(self):
        self.assertEqual(
            5,
            self._puzzle_game.get_tile(2, 2)
        )

    def test_raises_invalid_position_when_calling_get_tile_with_column_above_board_number_of_columns(self):
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(1, 4)

    def test_raises_invalid_position_when_calling_get_tile_with_negative_column(self):
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(1, -1)

    def test_raises_invalid_position_when_calling_get_tile_with_line_above_board_number_of_lines(self):
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(4, 1)

    def test_raises_invalid_position_when_calling_get_tile_with_negative_line(self):
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(-1, 1)
