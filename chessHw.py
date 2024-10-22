#hi all
from random import randint
import chess
import datetime

# board = chess.Board()

def computerChooseMove(board):
  legal_moves = list(board.legal_moves)
  capture_moves = []
  for move in legal_moves:
    if board.is_capture(move):
      capture_moves.append(move)
  
  if not capture_moves: #if list is empty
    random_move = legal_moves[randint(0, len(legal_moves)-1)]
  else:
    random_move = capture_moves[randint(0, len(capture_moves)-1)]
  return random_move


  #If one or more moves are available which capture an enemy piece, 
  # your program should always choose one of the capture moves.  Otherwise, program should 
  # randomly choose a move from among all of the available valid moves. 
  

def computerWhite(board):
  #do the first move, f2f4
  # first_move = chess.Move.from_uci("f2f4")

  while board.outcome() is None:

    first_move = computerChooseMove(board)
    print("computer move (white): ", first_move)
    board.push(first_move)
    print(board.fen())
    print(board)
    if board.is_checkmate():
      print("Checkmate!")
    if board.outcome() is not None:
      break


    #Black makes move
    black_first_move = chess.Move.from_uci(input('Black: '))
    while black_first_move not in board.legal_moves:
      black_first_move = chess.Move.from_uci(input('Move not legal. Pls enter new move: '))
    board.push(black_first_move)
    print("New FEN Position: " + board.fen())
    print(board)

  
  return board

  

  # computerChooseMove(board.fen(), board)

def computerBlack(board):
  while (board.outcome()) is not None:

    #white makes first move
    white_first_move = chess.Move.from_uci(input('White: '))
    while white_first_move not in board.legal_moves:
      white_first_move = chess.Move.from_uci(input('Move not legal. Pls enter new move: '))
    board.push(white_first_move)
    print("New FEN Position: " + board.fen())
    print(board)
    if board.is_checkmate():
      print("Checkmate!")
    if board.outcome():
      break

    first_move = computerChooseMove(board)
    print("computer move (black): ", first_move)
    board.push(first_move)
    print(board.fen())
    print(board)

  return board


def botsPlay(board):
  #do the first move, f2f4
  # first_move = chess.Move.from_uci("f2f4")

  while not board.outcome():

    first_move = computerChooseMove(board)
    print("computer move (white): ", first_move)
    board.push(first_move)
    print(board.fen())
    print(board)
    if board.is_checkmate():
      print("Checkmate!")
    if board.outcome():
      break


    #Black makes move
    black_first_move = computerChooseMove(board)
    while black_first_move not in board.legal_moves:
      black_first_move = chess.Move.from_uci(input('Move not legal. Pls enter new move: '))
    board.push(black_first_move)
    print("New FEN Position: " + board.fen())
    print(board)
  
  

  return

def main():
  print('=====================================================\nCS 290 Chess Bot Version 0.1\n=====================================================')
  #date and time
  x = datetime.datetime.now()
  print('Time: ', x)
  computer_player = input('Computer Player (w=white/b=black): ')
  starting_FEN = input('Starting FEN position? (enter for standard starting position): ')
  if starting_FEN == '':
    board = chess.Board()
  else:
    board = chess.Board(starting_FEN)
  print(board)
  print(board.fen())
  if computer_player == 'w':
    computerWhite(board)
  elif computer_player == 'b':
    computerBlack(board)
  elif computer_player == 'bots':
    botsPlay(board)

  if board.is_stalemate():
    print("It's a tie!")
  elif board.is_insufficient_material():
    print("Neither side has sufficient enough material to win!")
  
  #in a loop:
  #white move, new fen, black moves, new fen.
  #maybe after ea move, should check if anyone has won or sth? and before ea computer turn, the computer needs a list of moves (board.legal_moves)

if __name__ == "__main__":
  main()