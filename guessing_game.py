from random import randint

computer = randint(1,10)
keep_playing = None

while keep_playing != 'n':
  user = int(input('Guess a number between 1 and 10: '))
  if user == computer:
    print('You got it!')
    keep_playing = input('Keep playing? (y/n) ')
    computer = randint(1,10)
  elif user > computer:
    print('Too high, try again!')
  else:
    print('Too low, try again!')
print('Good game!')
