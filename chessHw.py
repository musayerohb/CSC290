#hi all
from random import randint
import chess
import datetime

# board = chess.Board()

def computerChooseMove():
  pass

def startWhite():
  pass

def startBlack():
  pass



def main():
  print('=====================================================\nCS 290 Chess Bot Version 0.1\n=====================================================')
  #date and time
  x = datetime.datetime.now()
  print('Time: ', x)
  computer_player = input('Computer Player (w=white/b=black): ')
  starting_FEN = input('Starting FEN position? (enter for standard starting position): ')
  board = chess.Board()
  print(board)
  #in a loop:
  #white move, new fen, black moves, new fen.
  #maybe after ea move, should check if anyone has won or sth? and before ea computer turn, the computer needs a list of moves (board.legal_moves)

if __name__ == "__main__":
  main()