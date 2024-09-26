#hi all
import random
from random import randint


fsa1 = {
  'S':{0:'A'},
  'A':{0:'B', 'Accept':'Accept'},
  'B':{1:'A'}
}

fsa2 = {
  'S':{1:'A'},
  'A':{0:'B', '0':'D', 'Accept':'Accept'},
  'B':{1:'C'},
  'C':{1:'A'},
  'D':{0:'D', 'Accept':'Accept'}
}

def gen(fsa):
  
  word=''
  current_state = 'S'
  
  #start state = fsa[0]
  #choose item in dictionary, then append to word and go to that item. 
  list_of_letters = list(fsa[current_state].keys())
  next_letter = None 
  #loop over this
  while next_letter != 'Accept':
    next_letter = list_of_letters[randint(0, len(list_of_letters)-1)]
    current_state = fsa[current_state][next_letter]
    # word = word + next_letter
    if (next_letter == 'Accept'):
      print(word)
      return
    else:
      word += str(next_letter)
      list_of_letters = list(fsa[current_state].keys())

def main():
  gen(fsa1)
  gen(fsa2)

if __name__ == "__main__":
  main()