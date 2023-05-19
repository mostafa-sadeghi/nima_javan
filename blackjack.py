# blackjack or 21 game
# ASCII
# Unicode
# Kings , Queens , Jacks =>  10
# Aces  => 1 or 11
# Cards 2  -   10   => worth from 2 - 10
# H  =>  take another card
# S  =>  stop
# D  =>  Double

# print(ord('A'))
# print(chr(65))
# print(chr(9829))
# print(chr(9830))
# print(chr(9824))
# print(chr(9827))
import random

HEARTS = chr(9829)    # ♥
DIAMONDS = chr(9830)  # ♦
SPADES = chr(9824)    # ♠
CLUBS = chr(9827)     # ♣

BACKSIDE = 'backside'
money = 5000


def get_bet(money):
    while True:
        print(f'How much money do you want to bet? (1 - {money}) or `quit` ')
        bet = input('> ').lower()
        if bet == 'quit':
            print('Thanks for playing')
            exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= money:
            return bet


def generate_cards():
    '''generate all possible cards (52)'''
    all_cards = []  # [('J','♥'), ('Q','♥'), ....]
    for shape in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in ('J', 'Q', 'K', 'A'):
            all_cards.append((rank, shape))
        for rank in range(2, 11):
            all_cards.append((rank, shape))
    random.shuffle(all_cards)
    return all_cards


all_cards = generate_cards()
print(all_cards)
print(all_cards.pop())
print(all_cards)


# def main():
#     while True:  # main loop
#         # checking the money
#         if money <= 0:
#             print("No money!")
#             print("thanks for playing!")
#             exit()
#         # Begin bet
#         print("Money:", money)
#         bet = get_bet(money)

#         # give two cards to each player
#         all_cards = generate_cards()
#         # dealerHand =


# if __name__ == '__main__':
#     main()
