"""
test tictactoe_app_console.py from tictactoepackage with pytest
"""

import pytest

from tictactoeapp.tictactoe_app_console \
    import convert_board_coord_tuple_to_string, \
    convert_board_coord_string_to_tuple, main, ping

test = [
    ((1,1), "B2"), ((0,0), "A1"), ((0,2), "C1"), ((2,1), "B3")
]
@pytest.mark.parametrize("board_cell, expected_string", test)
def test_convert_board_coord_tuple_to_string(board_cell, expected_string):
    assert convert_board_coord_tuple_to_string(board_cell) == expected_string


test = [
    ("B2", (1,1)), ("A1", (0,0)), ("C1", (0,2)), ("B3", (2,1))
]
@pytest.mark.parametrize("string, expected_board_cell", test)
def test_convert_board_coord_string_to_tuple(string, expected_board_cell):
    assert convert_board_coord_string_to_tuple(string) == expected_board_cell


def test_ping():
    assert ping() == "pong"
