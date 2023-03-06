'''ROCK,SCISSORS,PAPER'''
import random
from random import randint,randrange
print('WELCOME TO ROCK,SCISSORS,PAPER GAME')
choice = (['rock','scissors','paper'])
user_input = input('please enter your choice').lower()
com_choice = choice[randint(0,2)]
print('Computer chose ' + com_choice)
if user_input == com_choice:
    print('draw')
elif user_input == 'rock'and com_choice == 'scissors':
    print('You win')
elif user_input == 'paper' and com_choice== 'scissors':
    print('Computer wins')
elif user_input == 'scissors' and com_choice == 'paper':
    print('you win')
elif user_input == 'scissors' and com_choice == 'rock':
    print('Computer wins')

'''GUESS THE NUMBER'''
print('WELCOME TO GUESS THE NUMBER GAME')
num = randrange(1,50)
user_guess = int(input('Guess a number between 1 and 50\n'))
trial = 0
while user_guess != num:
    if user_guess > num:
        print('Guess a lower number. Try again')
        user_guess = int(input('Guess a number between 1 and 50\n'))
    else:
        print('Guess a higher number. Try again')
        user_guess = int(input('Guess a number between 1 and 50\n'))
print('Well done,you guessed the right number')