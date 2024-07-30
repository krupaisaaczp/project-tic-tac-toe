def create_board():
  board = [[" " for _ in range(3)] for _ in range(3)]
  return board

def print_board(board):
  for row in board:
    print("|", end="")
    for cell in row:
      print(f" {cell} |", end="")
    print()

def is_valid_move(board, move):
  row, col = move
  return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def make_move(board, player, move):
  row, col = move
  board[row][col] = player

def check_win(board, player):
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True

  # Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True

  # Check diagonals
  if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
    return True

  return False

def check_draw(board):
  return all(cell != " " for row in board for cell in row)

def player_move(board):
  while True:
    try:
      row = int(input("Enter row (0-2): "))
      col = int(input("Enter column (0-2): "))
      move = (row, col)
      if is_valid_move(board, move):
        return move
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Please enter numbers.")

def main():
  board = create_board()
  players = ["X", "O"]
  current_player = 0

  while True:
    print_board(board)
    player = players[current_player]
    print(f"Player {player}'s turn")
    move = player_move(board)
    make_move(board, player, move)

    if check_win(board, player):
      print_board(board)
      print(f"Player {player} wins!")
      break
    elif check_draw(board):
      print_board(board)
      print("It's a draw!")
      break

    current_player = (current_player + 1) % 2

if __name__ == "__main__":
  main()
