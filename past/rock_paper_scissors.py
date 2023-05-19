import random

ACTIONS = ("rock", "paper", "scissors")


def show_scores():
    print(f'{"player":<12}{"Score":>10}')
    print(f'{"me":<12}{player_score:>10}')
    print(f'{"computer":<12}{computer_score:>10}')


print('''Welcome to Rock Paper Scissors Game.
Game's Rule
''')
print('To Start the game press enter...')
input('> ')

status = True

computer_score = 0
player_score = 0
while status:
    computer_hand = random.choice(ACTIONS)

    print('Enter (Rock:"1") or (Paper:"2") or (Scissors:"3")')
    user_input = ''
    while (not user_input.isdecimal()) or (user_input not in ('1', '2', '3')):
        print('enter "1" or "2" or "3" ')
        user_input = input('> ')
    player_hand = ACTIONS[int(user_input)-1]

    print('computer\'s hand:', computer_hand)
    print('player\'s hand:', player_hand)

    # player winning states

    if player_hand == 'rock' and computer_hand == 'scissors':
        player_score += 1
        show_scores()

    elif player_hand == 'scissors' and computer_hand == 'paper':
        player_score += 1
        show_scores()

    elif player_hand == 'paper' and computer_hand == 'rock':
        player_score += 1
        show_scores()

    # computers winning states

    elif computer_hand == 'rock' and player_hand == 'scissors':
        computer_score += 1
        show_scores()

    elif computer_hand == 'scissors' and player_hand == 'paper':
        computer_score += 1
        show_scores()

    elif computer_hand == 'paper' and player_hand == 'rock':
        computer_score += 1
        show_scores()
    else:
        show_scores()

    print("Do you want to continue (Yes or No)")
    if input('> ').lower().startswith('n'):
        show_scores()
        input('press enter to exit> ')
        status = False
