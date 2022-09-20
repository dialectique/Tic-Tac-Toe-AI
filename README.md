# Tic-Tac-Toe app
- Tic-Tac-Toe game for on human player.
  - https://fr.wikipedia.org/wiki/Tic-tac-toe
- AI implemented with minimax algorithm optimized with alpha-beta pruning.
  - https://en.wikipedia.org/wiki/Minimax
  - https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- Since Tic-Tac-Toe is a tie given optimal play by both sides, it is not possible to beat the AI... But the AI can win if the human doesn't play optimally.
- The game has for now a simple implementation in the console.

## Installation
- It is recommended to use a virtual environment to install this project
- If setuptools is already installed, execute the following command line: ```make install```
- If setuptools is not installed, execute the followin command line: ```pip install setuptools``` then ```make install```
- Check out Makefile for more usefull command lines

## Usage:
- From the root oh the project, execute: ```tictactoeapp/tictactoe_app_console.py```

## How to play
- The user choose to play "X" or "O".
- "X" always starts.
- At each turn:
  - if it's human's turn: the human choose an empty cell.
  - if it's computer's turn: the MiniMax AI choose an empty cell.

## Tests
- Run ```make tests```

## Further improvement
- The game implementation in the console is very simple.
- Simple web app coming soon.
