import random
# n = int(input('enter a number:'))
# print("your number is:", n)
digit_posiotion = ["first", "second", "third", "forth",
                   "fifth", "sixth", "seventh", "eightth", "nineth", "tens"]
# i = 0
# while (n != 0):
#     m = n % 10
#     print(f"{digit_posiotion[i]} digit is:", m, end="\t")
#     n = n // 10
#     i += 1


def check_unique_digits(numbers):
    status = True
    for i in range(len(numbers)):
        if numbers[i] in numbers[i+1:]:
            status = False
    return status


result = check_unique_digits([1, 2, 0])
print(result)


def generate_secret_number():
    n = random.randrange(100, 1000)
    print("actual number is:", n)
    # i = 0
    numbers = []
    while (n != 0):
        m = n % 10
        numbers.append(m)
        # print(f"{digit_posiotion[i]} digit is:", m, end="\t")
        n = n // 10
        # i += 1
    print(numbers)


# generate_secret_number()
