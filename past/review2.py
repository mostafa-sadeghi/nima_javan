# a = 4
# b = 4
# Basic comparisons
# if a < b:
#  print("a is less than b")
# if a > b:
#  print("a is greater than b")
# print("Done")


# if a <= b:
#     print("a is less than or equal to b")
# if a >= b:
#     print("a is greater than or equal to b")

# a = 4
# b = 4
# if a == b:
#  print("a is equal to b")
# # Not equal
# if a != b:
#  print("a and b are not equal")

# if not a==b:
#  print("a and b are not equal")

# name = input("enter students's name:> ")
# age = int(input("enter students's age:> "))

# if age < 8:
#     print(f'{name} is kid.')
# if age >= 8 and age < 13:
#     print(f'{name} is junior.')
# # if 8 <= age < 13:
# #     print(f'{name} is junior.')
# if age >= 13 and age < 18:
#     print(f'{name} is teenager.')
# else:
#     print(f'{name} is adult.')


# if True and True and True:
#     print('*******')
# if True and False:
#     print('*******')
# if False and True:
#     print('*******')
# if False and False:
#     print('*******')


# if True or True or True:
#     print('*******')
# if True or False:
#     print('*******')
# if False or True:
#     print('*******')
# if False or False:
#     print('*******')


# a = True
# if a:
#     print(True)
# if True:
#     print(True)


# if 1 < 2:
#     print("ok")

# if True:
#     print("ok")
# if 1 > 2:
#     print("ok")


# a = True
# if not a:
#     print('*')


# a = False
# if not a:
#     print('*')


# a = 3
# b = 3
# c = a == b
# print(c)


# if 1:
#     print("1")

# if 0:
#     print("0")
# if -1:
#     print("-1")
# print(bool(1))
# print(bool(0))
# print(bool(-1))

# if '':
#     print("something")
# if 'a':
#     print("siklflksfds")


# USER = 'root'
# PASSWD = 'root'

# user_name = input('enter the user name:> ')
# password = input('enter the password:> ')
# if user_name and password:
#     if user_name == USER and password == PASSWD:
#         print('you can login now')
#     else:
#         print('user name or password is not correct...')


# else:
#     print('you must enter your user name and/or password')


# entry = input('enter a name or "exit" to exit from program:> ')
# if entry == 'exit':
#     print('good bye')
#     exit()
# print("balalall")
# if True:
#     print("ok")


# USER = ['root', 'admin']
# PASSWD = 'root'

# user_name = input('enter the user name:> ')
# password = input('enter the password:> ')
# if user_name and password:
#     if (user_name == 'root' or user_name == 'admin') and password == PASSWD:
#         print('you can login now')
#     else:
#         print('user name or password is not correct...')


# else:
#     print('you must enter your user name and/or password')


#################################################################

# user_name = input('enter your user name:> ')
# if user_name.lower() == 'nima':
#     print("you are valid user.")
# else:
#     print("you are not valid user.")


# کدام شرط می گوید که
# a < b


# a. if a less than b:
# b. if a < b
# c. if a > b
# d. if a < b:
# e. if (a < b)
# f. if a >= b
# g. if a <= b:


# برابری

# a. if a equals b:
# b. if a = b
# c. if a = b:
# d. if a == b:
# e. if a == b
# f. if a === b
# g. if a === b:


# کوچکتر یا مساوی

# a. if a < or = b:
# b. if a <= b:
# c. if a < = b:
# d. if a >= b:
# e. if a =< b:
# f. if a < b or == b:
# g. if a <== b:

# a
# هم از
# b
# کوچکتر است
# هم از
# c

# a. if a < b and < c:
# b. if a < b & c:
# c. if a < b and a < c:
# d. if a < b and c:


# a = 2
# b = 3
# c = 4
# if a < b & c:
#     print("ok")


# print("3" == "3")


# print(" 3" == "3")
# print(len(" 3"))
# print(len("3"))
# for s in " 3":
#     print(s)
# print("----------------------")
# for s in "3":
#     print(s)


# print(3 < 4)


# print(3 < 10)


# print("3" < "4")
# print("ali" < "maryam")
# print("sima" < "tina")
# print("nima" < "maryam")

# print(ord('3'))
# print(ord('4'))

# print("3" < "10")
# print(ord('3'))
# print(ord('1'))


# print((2 == 2) == "True")
# True == "True"
# print(type(True))
# print(type("True"))

# print((2 == 2) == True)


# print(3 < "3")  # Error
# print(3 == "3")
# print(3 <= "3")  # error
# print('2' <= "3")
# print('3' <= "3")
# print('ali' <= "reza")
# print('ali' <= "ali")

'''
یک عدد را از ورودی بگیری
و 
اگر عدد بر سه بخش پذیر بود؟
fizz
را پرینت کند

اگر بر پنج بخش پذیر بود

buzz را پرینت کند
اگر بر هر دو بخش پذیر بود
fizzbuzz
'''
number = int(input('enter a number:> '))
# write a function that takes number as parameter and do above describtion
# function returns fizz or buzz or fizzbuzz


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    elif num % 3 == 0:
        return "Fizz"

    elif num % 5 == 0:
        return "Buzz"


print(fizz_buzz(number))


'''
عدد از ورودی  n = 3
oooooo
o    o
oooooo
عدد از ورودی  n = 8
oooooooooooooooo
o              o
o              o
o              o
o              o
o              o
o              o
oooooooooooooooo

'''
