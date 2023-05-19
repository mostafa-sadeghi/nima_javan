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


def is_unique_digits(numbers):
    status = True
    for i in range(len(numbers)):
        if numbers[i] in numbers[i+1:]:
            status = False
            break
    return status


def generate_secret_number():
    n = random.randrange(100, 1000)
    # print("actual number is:", n)
    # i = 0
    numbers = []
    while (n != 0):
        m = n % 10
        numbers.append(m)
        # print(f"{digit_posiotion[i]} digit is:", m, end="\t")
        n = n // 10
        # i += 1
    numbers.reverse()
    return numbers


sec_num = generate_secret_number()
while not is_unique_digits(sec_num):
    sec_num = generate_secret_number()
print(sec_num)
