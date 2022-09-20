"""
test tictactoe.py from tictactoepackage with pytest
"""

import pytest
from tictactoeapp.tictactoe_ai import Tictactoe, main

ttt = Tictactoe()

EMPTY_BOARD = [[None, None, None,],
            [None, None, None,],
            [None, None, None,]]

def test_initial_state():
    assert ttt.initial_state() == EMPTY_BOARD

def test_player_empty_board():
    assert ttt.player(EMPTY_BOARD) == "X"

def test_player_next_player_X():
    board = [[None, "X", None,],
            [None, "O", None,],
            [None, None, None,]]
    assert ttt.player(board) == "X"

def test_player_next_player_O():
    board = [["X", "X", None,],
            [None, "O", None,],
            [None, None, None,]]
    assert ttt.player(board) == "O"

def test_actions_empty_board():
    assert ttt.actions(EMPTY_BOARD) == {
        (0,0), (0,1), (0,2),
        (1,0), (1,1), (1,2),
        (2,0), (2,1), (2,2)
    }

def test_actions_random_board():
    board = [["X", "X", "O",],
            [None, "O", None,],
            ["X", None, None,]]
    assert ttt.actions(board) == {
        (1,0), (1,2), (2,1), (2,2)
    }

def test_actions_full_board():
    board = [["X", "X", "O"],
            ["O", "O", "X"],
            ["X", "O", "X"]]
    assert ttt.actions(board) == set()

def test_result_empty_board():
    assert ttt.result(EMPTY_BOARD, (1,2)) == [
        [None, None, None],
        [None, None, "X"],
        [None, None, None]
    ]

def test_result_random_board():
    board = [["X", "X", "O",],
            [None, None, "O",],
            ["X", None, None,]]
    assert ttt.result(board, (1,1)) == [
        ["X", "X", "O",],
        [None, "O", "O",],
        ["X", None, None,]
    ]

def test_result_full_board():
    board = [["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"]]
    with pytest.raises(ValueError):
        ttt.result(board, (2,1))

def test_winner_X_win_diag1():
    board = [["X", "O", None],
            ["O", "X", "O"],
            ["X", "O", "X"]]
    assert ttt.winner(board) == "X"

def test_winner_X_win_diag2():
    board = [[None, "O", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"]]
    assert ttt.winner(board) == "X"

def test_winner_O_win_line1():
    board = [["O", "O", "O"],
            ["X", "X", None],
            [None, None, None]]
    assert ttt.winner(board) == "O"

def test_winner_O_win_line2():
    board = [["X", "X", None],
            ["O", "O", "O"],
            [None, None, None]]
    assert ttt.winner(board) == "O"

def test_winner_O_win_line3():
    board = [["X", "X", None],
            [None, None, None],
            ["O", "O", "O"]]
    assert ttt.winner(board) == "O"

def test_winner_no_winner():
    board = [["X", "X", "O"],
            ["O", "O", "X"],
            ["X", "O", "X"]]
    assert ttt.winner(board) == None

def test_winner_X_win_col1():
    board = [["X", "O", None],
            ["X", None, "O"],
            ["X", "O", "X"]]
    assert ttt.winner(board) == "X"

def test_winner_X_win_col2():
    board = [["O", "X", None],
            [None, "X", "O"],
            ["O", "X", "X"]]
    assert ttt.winner(board) == "X"

def test_winner_X_win_col3():
    board = [["O", None, "X"],
            [None, "O", "X"],
            ["O", "X", "X"]]
    assert ttt.winner(board) == "X"

def test_terminal_game_is_over():
    board = [["O", "O", "X"],
            ["X", "O", "X"],
            ["O", "X", "X"]]
    assert ttt.terminal(board) == True

def test_terminal_game_is_not_over():
    board = [["O", "O", "X"],
            ["X", "O", None],
            [None, "X", "X"]]
    assert ttt.terminal(board) == False

def test_minimax1():
    board = [["O", "O", "X"],
            ["X", "X", None],
            ["O", None, None]]
    assert ttt.minimax(board) == (1,2)

def test_minimax2():
    board = [["X", "X", "O"],
            [None, None, "X"],
            [None, "O", "O"]]
    assert ttt.minimax(board) == (2,0)

def test_minimax3():
    board = [["X", "X", "O"],
            [None, "O", None],
            [None, None, None]]
    assert ttt.minimax(board) == (2,0)

def test_ping():
    assert ttt.ping() == "pong"

def test_main():
    assert main() == None
