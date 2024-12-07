import unittest

from src.puzzle_game import PuzzleGame
from src.invalid_position_exception import InvalidPositionException
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To12345X786

# All-c-uses / Some-p-uses
# A) 1 - 2 - 3 - 6

class TestAllCUsesSomePUses(unittest.TestCase):
    def setUp(self) -> None:
        self._puzzle_game = PuzzleGame(3)
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(self._puzzle_game)

    def test_returns_board_tile_when_tile_is_valid_and_not_empty(self):
        # A) 1 - 2 - 3 - 6
        self.assertEqual(
            5,
            self._puzzle_game.get_tile(2, 2)
        )
