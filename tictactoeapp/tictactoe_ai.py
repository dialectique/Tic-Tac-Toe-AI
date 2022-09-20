import math
import random
from copy import deepcopy


class Tictactoe:
    """
    A class for tic-tac-toe AI implemented with Minimax algorithm
    and optimized with alpha-beta pruning.
    """
    # class constant, which represent the board's cells possible values
    X = "X"
    O = "O"
    EMPTY = None


    def initial_state(self):
        """
        Returns starting state of the board.
        :return: nested list (3*3)
        :rtype: list
        """
        return [[self.EMPTY, self.EMPTY, self.EMPTY],
                [self.EMPTY, self.EMPTY, self.EMPTY],
                [self.EMPTY, self.EMPTY, self.EMPTY]]


    def player(self, board):
        """
        Check who is the player who has the next turn on a board.
        :param board: board
        :type board: list
        :return: player who has the next turn on a board.
        :rtype: str

        """
        # Flatten the boars into one list only
        flatten_board = sum(board, [])

        # X starts the game. If the board is empty, return X.
        if flatten_board.count(self.EMPTY) == 9:
            return self.X

        # If number of X = number of O, next turn will be X
        return self.X if flatten_board.count(self.X) == \
            flatten_board.count(self.O) else self.O


    def actions(self, board):
        """
        Get all possible actions available on the board.
        :param board: board
        :type board: list
        :return: set of all possible actions (i, j) available on the board.
        :rtype: set
        """
        # For all the board's cells: check if it is empty,
        # add the empty cell coordinates in the set to be returned and
        # return the set.
        possible_actions = [
            (i, j) for i in range(3) for j in range(3) if board[i][j] == self.EMPTY
        ]
        return set(possible_actions)


    def result(self, board, action):
        """
        Returns the board that results from making move (i, j) on the board.
        :param board: board
        :type board: list
        :param action: move on the board
        :type action: tuple
        :raise ValueError: if cell (i,j) is not empty
        :return: board that results from making move (i, j) on the board.
        :rtype: list
        """
        # get i and j:
        i, j = action

        # Check if the action is valid (i.e. (i,j) cell is EMPTY)
        # and raise an exception if action is not valid.
        if board[i][j] != self.EMPTY:
            raise ValueError

        # Deep copy of the board
        result = deepcopy(board)

        # Get the player input for the next turn:
        player_input = self.player(board)

        # Update the result board by adding the player name in (i, j) cell
        result[i][j] = player_input

        # Return the updated board
        return result


    def winner(self, board):
        """
        Returns the winner of the game, if there is one.
        :param board: board
        :type board: list
        :return: the winner of the game, if there is one: "X", "O" or None
        :rtype: str
        """
        # For each player...
        for player in (self.X, self.O):

            # ...check if the player has a full row or a full column.
            for i in range(3):
                if all([board[i][j] == player for j in range(3)]) \
                        or all([board[j][i] == player for j in range(3)]):
                    return player

            # ...check if the player has a digonal.
            if all([board[i][i] == player for i in range(3)]) \
                    or all([board[i][2-i] == player for i in range(3)]):
                return player


    def terminal(self, board):
        """
        Returns True if game is over, False otherwise.
        :param board: board
        :type board: list
        :return: True or False
        :rtype: bool
        """
        # Returns True if there is a winner or if no more action is possible
        return True if self.winner(board) in (self.X, self.O) \
            or len(self.actions(board)) == 0 else False


    def utility(self, board):
        """
        Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
        :param board: board
        :type board: list
        :return: 1, -1 or 0
        :rtype: int
        """
        if self.winner(board) == self.X:
            return 1
        elif self.winner(board) == self.O:
            return -1
        return 0


    def max_value(self, board, alpha, beta):
        """
        Usefull function for the implementation of minimax
        optimized with alpha-beta pruning.
        Returns the max utility value for the next possible actions.
        :param board: board
        :type board: list
        :param alpha: best already explored option for X (maximizing player)
        :type alpha: int
        :parma beta: best already explored option for O (minimizing player)
        :type beta: int
        """
        # Check if the game is finished and return the winner
        if self.terminal(board):
            return self.utility(board)

        # Set max utility value to negative infinite (lowest possible)
        value = -math.inf

        # Get the set of all possible actions and convert it into a shuffled list
        # and set an empty list for the actions' values.
        possible_actions = list(self.actions(board))
        random.shuffle(possible_actions)
        possible_actions_values = []

        # For each possible action, get the maximum score of the next move
        # of the minimizing player O.
        for action in possible_actions:
            value = max(
                self.min_value(self.result(board, action), alpha, beta), value
                )
            possible_actions_values.append(value)

            # If value is greater or equal to the best value for O,
            # no need to continue to explore the other possible actions
            if value >= beta:
                break

            # update the best value for X
            alpha = max(alpha, value)

        # Return the maximum value of the possible actions
        return max(*possible_actions_values, -math.inf)


    def min_value(self, board, alpha, beta):
        """
        Usefull function for the implementation of minimax
        optimized with alpha-beta pruning.
        Returns the min utility value for the next possible actions.
        :param board: board
        :type board: list
        :param alpha: best already explored option for X (maximizing player)
        :type alpha: int
        :parma beta: best already explored option for O (minimizing player)
        :type beta: int
        """
        # Check if the game is finished and return the winner
        if self.terminal(board):
            return self.utility(board)

        # Set max utility value to positive infinite (highest possible)
        value = math.inf

        # Get the set of all possible actions and convert it into a shuffled list
        # and set an empty list for the actions' values.
        possible_actions = list(self.actions(board))
        random.shuffle(possible_actions)
        possible_actions_values = []

        # For each possible action, get the minimum score of the next move
        # of the maximazing player X.
        for action in possible_actions:
            value = min(
                self.max_value(self.result(board, action), alpha, beta), value
                )
            possible_actions_values.append(value)

            # If value is lower or equal to the best value for X,
            # no need to continue to explore the other possible actions
            if value <= alpha:
                break

            # update the best value for O
            beta = min(beta, value)

        # Return the minimum value of the possible actions
        return min(*possible_actions_values, value)


    def minimax(self, board):
        """
        Returns the optimal action for the current player on the board.
        Uses minimax optimized with alpha-beta pruning.
        :param board: board
        :type board: list
        :return: optimal action
        :rtype: tuple
        """
        # Return None if the game is over
        if self.terminal(board):
            return None

        # Get the player input for this coming turn
        player_input = self.player(board)

        # Get the next possible actions
        possible_actions = list(self.actions(board))
        random.shuffle(possible_actions)

        # Alpha-Beta Pruning:
        # Alpha is the best already explored option for X.
        # Beta is the best already explored option for O.
        # Initialisation to the 'worst score' for X and O:
        # set alpha to negative infinity and beta to positive infinity.
        alpha = -math.inf
        beta = math.inf

        # If player is X, return the action that produce the highest value
        # of the min_value function.
        if player_input == self.X:
            possible_actions_min_score = [
                self.min_value(
                    self.result(board, action), alpha, beta
                    ) for action in possible_actions
                ]
            return possible_actions[
                possible_actions_min_score.index(max(possible_actions_min_score))]

        # If player is O, return the action that produce the lowest value
        # of the max_value function.
        else:
            possible_actions_max_score = [
                self.max_value(
                    self.result(board, action), alpha, beta
                    ) for action in possible_actions
                ]
            return possible_actions[
                possible_actions_max_score.index(min(possible_actions_max_score))]


    def ping(self):
        """
        You call ping I return pong.
        """
        return "pong"


def main():
    print("The library tictactoe.py has been ran directly.")


if __name__ == "__main__":
    main()
