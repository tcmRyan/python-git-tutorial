#!/bin/python3

from random import randint

def play(p_score, c_score):
    
    print('Welcome to Rock, Paper, Scissors!')
    print('The score is player: {}, computer: {}'
    .format(p_score, c_score))
    player = input('rock (r), paper (p) or scissors (s)?')

    if player == 'r':
      print('O', end=' ')
      
    elif player == 'p':
      print('___', end=' ')
      
    elif player == 's':
      print('>8', end=' ')
      
    else:
      print('??')
      
    print('vs', end=' ')

    chosen = randint(1,3)

    if chosen == 1 :
      computer = 'r'
      print('O')
      
    elif chosen == 2 :
      computer = 'p'
      print('___')
      
    else:
      computer = 's'
      print('>8')

    if player == computer:
      print('DRAW!')
      
    elif player == 'r' and computer == 's':
      print('Player wins!')
      p_score = p_score + 1
      
    elif player == 'r' and computer == 'p':
      print('Computer wins!')
      c_score = c_score + 1
      
    elif player == 'p' and computer == 'r':
      print('Player wins!')
      p_score = p_score + 1
      
    elif player == 'p' and computer == 's':
      print('Computer wins!')
      c_score = c_score + 1

    elif player == 's' and computer == 'p':
      print('Player wins!')
      p_score = p_score + 1
      
    elif player == "s" and computer == 'r':
      print('Computer wins!')
      c_score = c_score + 1

    else:
      print('Huh?')
    
    keep_playing = input('Would you like to play again? y/n')
    if keep_playing == 'y':
        play(p_score, c_score)
    else:
        if p_score > c_score:
            print('Player wins with a final score of {}'.format(p_score))
        elif p_score < c_score:
            print('Computer wins with a final score of {}'.format(c_score))
        else:
            print("No winner, it's a draw!")
        print('Thanks for playing')

play(0,0)

