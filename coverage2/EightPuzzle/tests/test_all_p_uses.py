import unittest

from src.puzzle_game import PuzzleGame
from src.invalid_position_exception import InvalidPositionException
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To12345X786

# All-p-uses
# A) 1 - 2 - 3 - 5
# B) 1 - 2 - 3 - 6
# C) 1 - 2 - 4

class TestAllPUses(unittest.TestCase):
    def setUp(self) -> None:
        self._puzzle_game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(self._puzzle_game)

    def test_returns_empty_when_tile_is_empty(self):
        # A) 1 - 2 - 3 - 5
        self.assertEqual(
            " ",
            self._puzzle_game.get_tile(2, 3)
        )

    def test_returns_board_tile_when_tile_is_valid_and_not_empty(self):
        # B) 1 - 2 - 3 - 6
        self.assertEqual(
            5,
            self._puzzle_game.get_tile(2, 2)
        )

    def test_raises_invalid_position_when_line_and_column_are_negative(self):
        # C) 1 - 2 - 4
        with self.assertRaises(InvalidPositionException):
            self._puzzle_game.get_tile(-1, -1)