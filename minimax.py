import random
# positive infinity
p_inf = float("inf")
# negative infinity
n_inf = float("-inf")

board = [
  ['', '', ''],
  ['', '', ''],
  ['', '', '']

];


ai = 'X'
human = 'O'
currentPlayer = human


def three_in_a_row(a, b, c):
  return a !='' and a == b and b == c


def checkWinner():
  winner = None

  for i in range(0,3):
    if three_in_a_row(board[i][0], board[i][1], board[i][2]):
      winner = board[i][0]  

  for i in range(0,3):
    if three_in_a_row(board[0][i], board[1][i], board[2][i]):
      winner = board[0][i]

  if three_in_a_row(board[0][0], board[1][1], board[2][2]):
    winner = board[0][0]
  
  if three_in_a_row(board[2][0], board[1][1], board[0][2]):
    winner = board[2][0]
  

  openSpots = 0
  for i in range(0,3):
    for j in range(0,3):
      if (board[i][j] == ''):
        openSpots+=1

  if winner == None and openSpots == 0:
    return 'tie'
  else:
    return winner




def minimax(board, depth, isMaximizing):
  result = checkWinner()
  if (result != None):
    return scores[result]

  if (isMaximizing):
    bestScore = n_inf
    for i in range(0,3):
      for j in range(0,3):
        if board[i][j] == '':
          board[i][j] = ai;
          score = minimax(board, depth + 1, False);
          board[i][j] = '';
          bestScore = max(score, bestScore);
    return bestScore;
  else:
    bestScore = p_inf
    for i in range(0,3):
      for j in range(0,3):
        if board[i][j] == '':
          board[i][j] = human;
          score = minimax(board, depth + 1, True)
          board[i][j] = ''
          bestScore = min(score, bestScore);

    return bestScore



def bestMove():
  bestScore = n_inf
  for i in range(0,3):
    for j in range(0,3):
      if (board[i][j] == ''):
        board[i][j] = ai
        score = minimax(board, 0, False)
        board[i][j] = ''
        if (score > bestScore):
          bestScore = score
          move = { "i":i, "j":j }
  board[move["i"]][move["j"]] = ai
  currentPlayer = human


scores = {'X': 10,'O': -10,'tie': 0}


def main ():
 input1=" "
 print("AI moves first!")
 i=random.randint(0, 2) 
 j=random.randint(0, 2)
 board[i][j]='O'
 bestMove()
 while not input1 =="":
  for i in range(0,3):
    print("  " + board[i][0] + "  |  " + board[i][1]  + "  |  " + board[i][2] +"  ")
    if i < 2:
      print(" ============== ")
  w=checkWinner()
  if w != None:
      print("Winner is " + w)
      break
  print("Which cell would you like to put an 'O' in?  starting from top left:0,0 0,1 0,2 1,0 1,1 1,2 2,0 2,1 2,2")
  input1 = input() 
  if int(input1[0]) < 3 and int(input1[2]) < 3 and board[int(input1[0])][int(input1[2])] =='':
          board[int(input1[0])][int(input1[2])] = human
          w=checkWinner()
          if w != None:
              print("Winner is " + w)
              break
          currentPlayer = ai
          bestMove()

main()

