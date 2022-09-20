"""
Very simple Tic-Tac-Toe game implementation in console.
AI implemented with Minimax algorithm and optimized with alpha-beta pruning.
Check tictactoeapp/tictactoe_ai.py for more details.
"""

from tictactoeapp.tictactoe_ai import Tictactoe

ttt = Tictactoe()

def display(board):
    """
    Display the game's board in the console
    """
    dict = {'X': ' X ', 'O': ' O ', None: '   '}
    print("\n      | A | B | C |")
    print("   ----------------")
    print(f"    1 |{dict[board[0][0]]}|{dict[board[0][1]]}|{dict[board[0][2]]}|")
    print("   ----------------")
    print(f"    2 |{dict[board[1][0]]}|{dict[board[1][1]]}|{dict[board[1][2]]}|")
    print("   ----------------")
    print(f"    3 |{dict[board[2][0]]}|{dict[board[2][1]]}|{dict[board[2][2]]}|")
    print("   ----------------\n")


def convert_board_coord_tuple_to_string(cell):
    """
    Convert board cell coordinate from (i,j) to string.
    Example: (0,0) -> "A1"     (1,2) -> "C2"
    """
    dict = {(0,0): "A1", (0,1): "B1", (0,2): "C1",
            (1,0): "A2", (1,1): "B2", (1,2): "C2",
            (2,0): "A3", (2,1): "B3", (2,2): "C3"}
    return dict[cell]


def convert_board_coord_string_to_tuple(string):
    """
    Convert board cell coordinate from string to (i,j).
    Example: "A1" -> (0,0)    "C2" -> (1,2)
    """
    dict = {"A1": (0,0), "B1": (0,1), "C1": (0,2),
            "A2": (1,0), "B2": (1,1), "C2": (1,2),
            "A3": (2,0), "B3": (2,1), "C3": (2,2)}
    return dict[string]


def main():
    # Tic-Tac-Toe game start.
    print("\nTic-Tac-Toe - Human vs A.I.\n")

    # Initialise board
    board = ttt.initial_state()

    # Ask the user to choose the starting player.
    starting_player = ""
    print("Who starts the game? Human (h) or Computer (c) ?")
    while starting_player not in ("h", "c"):
        starting_player = input('Please enter "h" or "c": ')

    # X starts the game. Set-up X and O depending of the choosen starting player.
    if starting_player == "h":
        human, computer = "X", "O"
    else:
        human, computer = "O", "X"

    # Turn vatiable is used to count the number of turns. 1 <= turn <= 9.
    turn = 1

    # Game loop
    while True:
        # Display the turn number and players (X or O, for human and computer)
        # and display the board.
        print(f"\n-------- Turn {turn} --------")
        print(f"Human: {human} --- Computer: {computer}")
        display(board)

        # Get who is the current turn player.
        # Get and display the possible actions .
        player = ttt.player(board)
        possible_actions = sorted(
            [convert_board_coord_tuple_to_string(action) for action in ttt.actions(board)]
            )
        print(f"Player {player}, please choose a cell among: ")
        print(", ".join(possible_actions))

        # If current player is human: ask for the player's action (i.e. choose empty cell)
        if player == human:
            action = ""
            while action not in possible_actions:
                action = input("Please enter a valid cell: ").upper()
            print(f"Human choose {action}")
            action = convert_board_coord_string_to_tuple(action)
        # If current player is computer: get the action from minimax AI,
        # i.e. choose the best empty cell.
        else:
            action = ttt.minimax(board)
            print(f"Computer choose {convert_board_coord_tuple_to_string(action)}")

        # Implement the action to the board.
        board = ttt.result(board, action)

        # If game is over, exit the game loop.
        if ttt.terminal(board):
            break

        # End of the current turn. Increment turn.
        turn += 1

    # Check who is the winner and display it. If Tie, display "Tie"
    # Since Tic-Tac-Toe is a tie given optimal play by both sides,
    # It is not possible to beat the AI... But the AI can win if the human
    # doesn't play optimally.
    winner = ttt.winner(board)
    print(f"\n------ Game Over -------")
    print(f"Human: {human} --- Computer: {computer}")
    display(board)
    if winner == None:
        print("Tie\n")
    else:
        print(f"The winner is {winner}\n")


def ping():
    """
    You call ping I return pong.
    """
    return "pong"
