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

    # Tests that kill mutants
    def test_raises_invalid_position_when_calling_get_tile_with_zero_line(self):
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(0, 1)

    def test_returns_valid_position_when_calling_get_tile_with_line_on_edge(self):
        self.assertEqual(
            7,
            self._puzzle_game.get_tile(3, 1)
        )

    def test_raises_invalid_position_when_calling_get_tile_with_zero_column(self):
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(1, 0)

    def test_returns_valid_tile_when_calling_get_tile_on_valid_lune_and_column_1(self):
        self.assertEqual(
            4,
            self._puzzle_game.get_tile(2, 1)
        )

    def test_moves_empty_tile_to_up_when_calling_move_empty_tile_with_up(self):
        self._puzzle_game.move_empty_tile('UP')

        self.assertEqual(
            " ",
            self._puzzle_game.get_tile(1, 3)
        )