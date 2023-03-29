# Tic-Tac-Toe game

# Initialize the board
board = [" " for i in range(9)]

def print_board():
  row1 = "|".join(board[0:3])
  row2 = "|".join(board[3:6])
  row3 = "|".join(board[6:9])

  print(row1)
  print("-" * 5)
  print(row2)
  print("-" * 5)
  print(row3)


# Function to check if the game is a draw
def check_draw():
  return not " " in board


# Function to check if a player has won
def check_win(player):
  win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                    (2, 5, 8), (0, 4, 8), (2, 4, 6)]
  for condition in win_conditions:
    if board[condition[0]] == player and board[
        condition[1]] == player and board[condition[2]] == player:
      return True
  return False


# Function to handle a player's turn
def player_turn(player):
  print_board()
  print(f"{player}'s turn. Which box? (1-9)")
  choice = int(input())
  if board[choice - 1] == " ":
    board[choice - 1] = player
  else:
    print("That box is already taken!")
    player_turn(player)


# Main game loop
player = "X"
while not check_win("X") and not check_win("O") and not check_draw():
  player_turn(player)
  if player == "X":
    player = "O"
  else:
    player = "X"

# Print final board and announce winner
print_board()
if check_win("X"):
  print("X wins!")
  print(" O loose \_/")
elif check_win("O"):
  print("O wins!")
  print(" X loose \_/ ")
else:
  print("It's a draw!")
  
