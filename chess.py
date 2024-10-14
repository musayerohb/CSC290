#hi all
from random import randint
import chessHw
from chessHw import *

# board = chess.Board()






def main():
  print('=====================================================/nCS 290 Chess Bot Version 0.1/n=====================================================')
  print('Time: ')
  computer_player = input('Computer Player (w=white/b=black): ')
  starting_FEN = input('Starting FEN position? (enter for standard starting position): ')
  board = chessHw.board()
  print(board)
  print('hi')
  #in a loop:
  #white move, new fen, black moves, new fen.
  #maybe after ea move, should check if anyone has won or sth? and before ea computer turn, the computer needs a list of moves (board.legal_moves)

if __name__ == "__main__":
  main()