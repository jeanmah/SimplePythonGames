import random
board = [ ["-"]*3 for r in range(3)] 
isTie = True

def printBoard():
  for row in board:
    formattedRow = ""
    for col in row:
      formattedRow +=(col + "|")
    print(formattedRow[:-1])

def getUserInput():
  isPossible = False
  while not isPossible:
    try:
      user_position = int(input("where do you want to put the X (0 to 8): "))
      if board[user_position//3][user_position%3] == "-":
        board[user_position//3][user_position%3] = "X"
        isPossible = True
      else:
        raise Exception("invalid input")
    except:
      print("please put a valid input")
      continue

def computerPosition():
  if (checkAlmostWins("O","X")):
    return
  if (checkAlmostWins("X","O")):
    return
  notPossible = True
  while notPossible:
    randIndex = random.randint(0,8)
    if board[randIndex//3][randIndex%3] == "-":
        board[randIndex//3][randIndex%3] = "O"
        notPossible = False

def checkAlmostWins(checkingPlayer,otherPlayer):
  partialWins = [0]*8
  #row1
  if board[0][0] ==checkingPlayer:
    partialWins[0] +=1
    partialWins[3] +=1
    partialWins[6] +=1
  elif board[0][0] ==otherPlayer:
    partialWins[0] = -3
    partialWins[3] = -3
    partialWins[6] = -3
  if board[0][1] ==checkingPlayer:
    partialWins[0] +=1
    partialWins[4] +=1
  elif board[0][1] ==otherPlayer:
    partialWins[0] = -3
    partialWins[4] = -3
  if board[0][2] ==checkingPlayer:
    partialWins[0] +=1
    partialWins[5] +=1
    partialWins[7] +=1
  elif board[0][2] ==otherPlayer:
    partialWins[0] = -3
    partialWins[5] = -3
    partialWins[7] = -3
  
  #row 2
  if board[1][0] ==checkingPlayer:
    partialWins[1] +=1
    partialWins[3] +=1
  elif board[1][0] ==otherPlayer:
    partialWins[1] = -3
    partialWins[3] = -3
  if board[1][1] ==checkingPlayer:
    partialWins[1] +=1
    partialWins[4] +=1
    partialWins[6] +=1
    partialWins[7] +=1

  elif board[1][1] ==otherPlayer:
    partialWins[1] = -3
    partialWins[4] = -3
    partialWins[6] = -3
    partialWins[7] = -3
  if board[1][2] ==checkingPlayer:
    partialWins[1] +=1
    partialWins[5] +=1
  elif board[1][2] ==otherPlayer:
    partialWins[1] = -3
    partialWins[5] = -3

  #row 3
  if board[2][0] ==checkingPlayer:
    partialWins[2] +=1
    partialWins[3] +=1
    partialWins[7] +=1
  elif board[2][0] ==otherPlayer:
    partialWins[2] = -3
    partialWins[3] = -3
    partialWins[7] = -3
  if board[2][1] ==checkingPlayer:
    partialWins[2] +=1
    partialWins[4] +=1
  elif board[2][1] ==otherPlayer:
    partialWins[2] = -3
    partialWins[4] = -3
  if board[2][2] ==checkingPlayer:
    partialWins[2] +=1
    partialWins[5] +=1
    partialWins[6] +=1
  elif board[2][2] ==otherPlayer:
    partialWins[2] = -3
    partialWins[5] = -3
    partialWins[6] = -3
  
  for i in range(8):
    if partialWins[i]==2:
      if i ==0:
        board[0][board[0].index("-")] = "O"
      elif i==1:
        board[1][board[1].index("-")] = "O"
      elif i==2:
        board[2][board[2].index("-")] = "O"
      elif i==3:
        if board[0][0] =="-":
          board[0][0] = "O"
        elif board[1][0] =="-":
          board[1][0] = "O"
        elif board[2][0] =="-":
          board[2][0] = "O"
      elif i==4:
        if board[0][1] =="-":
          board[0][1] = "O"
        elif board[1][1] =="-":
          board[1][1] = "O"
        elif board[2][1] =="-":
          board[2][1] = "O"
      elif i==5:
        if board[0][2] =="-":
          board[0][2] = "O"
        elif board[1][2] =="-":
          board[1][2] = "O"
        elif board[2][2] =="-":
          board[2][2] = "O"
      elif i==6:
        if board[0][0] =="-":
          board[0][0] = "O"
        elif board[1][1] =="-":
          board[1][1] = "O"
        elif board[2][2] =="-":
          board[2][2] = "O"
      elif i==7:
        if board[0][2] =="-":
          board[0][2] = "O"
        elif board[1][1] =="-":
          board[1][1] = "O"
        elif board[2][0] =="-":
          board[2][0] = "O"
      return True
  return False



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

while any("-" in row for row in board):
  getUserInput()
  if checkWin("X"):
    print("You Win!")
    isTie = False
    break
  computerPosition()
  if checkWin("O"):
    print("You Lose :(")
    isTie = False
    break
if isTie:
  print("Tie!")