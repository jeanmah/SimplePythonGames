import random
board = [ ["-"]*3 for r in range(3)] 
isTie = True
symbols = ["X","O"]

def printBoard():
  print(board[0][0] + "|" +board[0][1] + "|" +board[0][2])
  print(board[1][0] + "|" +board[1][1] + "|" +board[1][2])
  print(board[2][0] + "|" +board[2][1] + "|" +board[2][2])

def getUserInput(playerSymbol):
  isPossible = False
  while not isPossible:
    try:
      user_position = int(input("Where do you want to put the "+ playerSymbol +" (0 to 8): "))
      if board[user_position//3][user_position%3] == "-":
        board[user_position//3][user_position%3] = playerSymbol
        isPossible = True
      else:
        raise Exception("invalid input")
    except:
      print()
      print("Please put a valid input")
      continue


def checkWin(playerSymbol):
  printBoard()
  if (board[0][0]==playerSymbol and board[0][1]==playerSymbol and board[0][2]==playerSymbol):
      return True
  elif (board[1][0]==playerSymbol and board[1][1]==playerSymbol and board[1][2]==playerSymbol):
      return True
  elif (board[2][0]==playerSymbol and board[2][1]==playerSymbol and board[2][2]==playerSymbol):
      return True
  elif (board[0][0]==playerSymbol and board[1][0]==playerSymbol and board[2][0]==playerSymbol):
      return True
  elif (board[0][1]==playerSymbol and board[1][1]==playerSymbol and board[2][1]==playerSymbol):
      return True
  elif (board[0][2]==playerSymbol and board[1][2]==playerSymbol and board[2][2]==playerSymbol):
      return True
  elif (board[0][0]==playerSymbol and board[1][1]==playerSymbol and board[2][2]==playerSymbol):
      return True
  elif (board[0][2]==playerSymbol and board[1][1]==playerSymbol and board[2][0]==playerSymbol):
      return True
  else:
    return False

print("Tic-Tac-Toe")
for turn in range(9):
  print("\nPlayer " + str(turn%2+1)+"'s Turn")
  getUserInput(symbols[turn%2])
  if checkWin(symbols[turn%2]):
    print("Player " + str(turn%2+1)+" Wins!")
    isTie = False
    break
  
if isTie:
  print("Tie!")