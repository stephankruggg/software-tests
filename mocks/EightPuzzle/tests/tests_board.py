import unittest
from unittest.mock import patch

from src.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board(2, 2)
        self._board.put_tile(1, 1, 1)
        self._board.put_tile(2, 1, 2)
        self._board.put_tile(3, 2, 1)
        self._board.put_tile(None, 2, 2)
    
    def test_returns_none_when_calling_get_tile_with_line_and_column_of_none_without_mock(self):
        self.assertEqual(
            None,
            self._board.get_tile(2, 2)
        )

    @patch('src.board.Board.get_tile')
    def test_returns_none_when_calling_get_tile_with_line_and_column_of_none_with_mock(self, get_tile_mocked):
        get_tile_mocked.return_value = 5

        self.assertEqual(
            5,
            self._board.get_tile(2, 2)
        )

    def test_returns_1_when_calling_board_with_line_and_column_1_without_mock(self):
        self.assertEqual(
            1,
            self._board.get_tile(1, 1)
        )

    @patch('src.board.Board.get_tile')
    def test_returns_empty_tile_when_calling_get_tile_for_empty_position_with_mock(self, get_tile_mocked):
        get_tile_mocked.return_value = 1

        self.assertEqual(
            1,
            self._board.get_tile(1, 1)
        )
