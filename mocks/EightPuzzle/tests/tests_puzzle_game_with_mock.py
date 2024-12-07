import unittest
from unittest.mock import patch

from src.puzzle_game_with_mock import PuzzleGameWithPlayer
from tests.shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To12345X786


class TestPuzzleGameWithMock(unittest.TestCase):
    def setUp(self) -> None:
        self._puzzle_game = PuzzleGameWithPlayer(3, 'test')
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(self._puzzle_game)

    def test_returns_game_not_finished_when_game_is_equal_to_beginning_without_mock(self):
        self.assertEqual(
            'Game not finished',
            self._puzzle_game.end_of_the_game()
        )

    def test_returns_saved_when_game_is_finished_without_mock(self):
        self._puzzle_game.move_empty_tile('DOWN')

        self.assertEqual(
            'Saved',
            self._puzzle_game.end_of_the_game()
        )

    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_returns_saved_when_game_is_finished_with_mock(self, save_game_to_file_mocked):
        save_game_to_file_mocked.return_value = 'Saved'

        self._puzzle_game.move_empty_tile('DOWN')

        self.assertEqual(
            'Saved',
            self._puzzle_game.end_of_the_game()
        )

    @patch('src.puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file')
    def test_returns_game_not_finished_when_game_is_not_finished_with_mock(self, save_game_to_file_mocked):
        save_game_to_file_mocked.return_value = 'Saved'

        self.assertEqual(
            'Game not finished',
            self._puzzle_game.end_of_the_game()
        )
