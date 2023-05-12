# bitmap = """***********      *   ***   **   *       *******************************
#            ********************** **   **  *   *  ****************************** *
#         **        ******************           *******************************
#                    **************              **   *  ****  **  *********** *
#                      *********
#                         ******
#                       * ***  **
#                          **** *
#                           *******
#                         ********
#                             ********
# """

# message = input('> ')
# for line in bitmap.splitlines():
#     for i, pixel in enumerate(line):
#         if pixel == ' ':
#             print(' ', end='')
#         else:
#             print(message[i % len(message)], end='')
#     print()


# import turtle
# COLORS = ('red', 'green', 'blue')
# my_pen = turtle.Turtle()
# my_pen.speed('fast')
# my_pen.pensize(2)

# for j in range(12):
#     my_pen.pencolor(COLORS[j])  # error how to solve it with just three colors
#     for i in range(4):
#         my_pen.fd(100)
#         my_pen.left(90)
#     my_pen.left(30)


# turtle.done()

# MONTHS = "JanFebAprMarMayJunJulAugSepOctNovDec"

#  از شما خواسته شده اسم هر یک از ماه ها را از رشته بالا جدا کنید و در لیستی قرار دهید

months_list = []

# در انتها برنامه ای بنویسید که شماره ماه را از ورودی دریافت نماید و اسم ماه را نمایش دهد.


import string

# SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'

# برنامه ساخت رمز
# ورودی:
    #  string
    # کلید
# sara
# 1
# tbsb
SYMBOLS = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'

message = input('Enter a message to encrypt: ') # nima
key = int(input('Enter a key (0-25) ')) # 1
translated = ''
for char in message:
    char_index = SYMBOLS.find(char)
    char_index += key
    translated += SYMBOLS[char_index]

print(translated)


# exercise:
# رمز و کلید به شما داده می شود از طریق ورودی
# پیام اصلی را پرینت کن
# پیام:
# tbsb
# key : 1
# خروجی:
# sara


# zahra
#  2
# bcjtc