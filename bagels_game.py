import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''Welcome to our game, we are going to guess '{NUM_DIGITS}' digits number with no repeat digits.
    When I say :        That means:
        Pico                One digit is correct but not in right position.
        Fermi               One digit is correct and in right position.
        Bagels              No digit is correct.
        You have '{MAX_GUESSES}' times to guess the number!
    ''')
    while True:
        secret_number = generate_secret_number()
        print("secret number is:", secret_number)
        game_round = 1
        while game_round <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(
                    f"round {game_round}-->\tenter {NUM_DIGITS} digits number")
                guess = input('> ')
            hints = get_hint(guess, secret_number)
            print(hints)
            if guess == secret_number:
                break

            game_round += 1

        print("Do you want to continue? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Thank you for playing...")


def generate_secret_number():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += numbers[i]
    return secret_number


def get_hint(guess, secret_number):
    if guess == secret_number:
        return 'You got it!!!'
    hints = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            hints.append('fermi')
        elif guess[i] in secret_number:
            hints.append('pico')

    if (len(hints) == 0):
        return 'bagels'
    return hints


if __name__ == "__main__":
    main()


# exercise 1: یک لیست از اسامی دانش آموزا بساز و تعداد تکرار نام علی را مشخص کن و پرینت کن
# خروجی: 3
names = ['ali', 'tina', 'sima', 'matin', 'ali', 'java', 'ali']
# exe 2 : شماره ایندکس نام علی را پرینت کن
# خروجی :
# [0, 4, 6]
