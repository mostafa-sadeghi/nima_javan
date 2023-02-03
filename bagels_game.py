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


def generate_secret_number():
    pass


if __name__ == "__main__":
    # main()
    numbers = list('0123456789')
    random.shuffle(numbers)
    serect_number = ''
    for i in range(NUM_DIGITS):
        serect_number += numbers[i]
    print(serect_number)
