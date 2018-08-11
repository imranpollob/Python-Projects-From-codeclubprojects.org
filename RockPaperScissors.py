from random import randint

choice = input('Rock (r), Paper (p) or Scissors (s)? ')

if choice not in ['r', 'p', 's']:
    print('I can\'t understand your input')
    exit()

symbols = {
    1: 'Rock', 2: 'Paper', 3: 'Scissors',
    'r': 'Rock', 'p': 'Paper', 's': 'Scissors',
}

computer_choose = randint(1, 3)

player = symbols[choice]
computer = symbols[computer_choose]

print(player, "VS", computer)

if player == computer:
    print('DRAW!')


elif (player == 'Rock' and computer == 'Scissors') or \
     (player == 'Paper' and computer == 'Rock') or \
     (player == 'Scissors' and computer == 'Paper'):

    print("Player Wins!")

else:
    print("Computer Wins!")