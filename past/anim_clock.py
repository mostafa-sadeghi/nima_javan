# turtle document:
# https://docs.python.org/3/library/turtle.html
# convert to gif:
# https://cloudconvert.com/png-to-gif

# remove background
# https://www.remove.bg/

# import turtle

# s = turtle.Screen()
# s.title("my app")
# s.bgcolor('orange')
# s.bgpic('mario.png')
# s.register_shape('my_shape', ((10, 0), (10, 10), (0, 10), (0, 0)))
# s.register_shape("strawberry.gif")
# p = turtle.Pen()
# p.shape('my_shape')
# p.shape('strawberry.gif')
# p.shape('turtle')  # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
# p.setpos(200,200)
# p.forward(100)
# p.fd(100)
# p.bk(100)
# p.back(100)
# p.backward(100)
# p.pencolor("red")
# p.pensize(4)
# p.forward(100)
# p.left(90)

# p.forward(100)
# p.left(90)  # p.lt(90)
# p.forward(100)
# p.left(90)

# p.forward(100)
# p.left(90)

# p.forward(100)
# p.right(90)  # p.rt(90)
# p.forward(100)
# p.right(90)  # p.rt(90)
# p.forward(100)
# p.right(90)  # p.rt(90)
# p.forward(100)
# p.right(90)  # p.rt(90)

# p.left(90)
# p.forward(100)
# p.left(90)
# p.forward(100)
# p.left(90)
# p.forward(100)
# p.left(90)
# p.forward(100)


# p.right(90)
# p.forward(100)
# p.right(90)
# p.forward(100)
# p.right(90)
# p.forward(100)
# p.right(90)
# p.forward(100)


# p.setheading(45)  # p.seth(45)
# p.forward(200)
# s.exitonclick()
# print("END")


# excersise1
'''
مثلث
پنجضلعی
شش ضلعی
وستاره


'''

# import turtle
# name = "nikan"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# do this(iteration) with for loop
# for x in name:
#     print(x)


# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     print(n)
# numbers = (1, 2, 3, 4, 5)
# for n in numbers:
#     print(n)

# using range

# numbers = range(100)
# print(numbers)
# for y in numbers:
#     print(y)

# numbers = range(1, 101)
# for x in numbers:
#     print(x)

# numbers = range(1_000_000, 1_500_001)
# for n in numbers:
#     print(n)


# even number between 100_000 and 200_000
# even_numbers = []
# for number in range(100_000, 120_001, 2):
#     # print(number)
#     even_numbers.append(number)

# print(even_numbers)


# exercise 1
'''
با کمک حلقه فور برنامه ای بنویس که 5 عدد از ورودی دریافت نماید و حاصل جمع آنها را نمایش دهد


'''


# total = 0
# for i in range(5):
#     number = float(input(f'Enter number {i+1} > '))
#     total += number
#     # total = total + numbers

# print(f'sum of 5 numbers is: {total:.2f}')


# x = '1.2'
# z = float(x) + 3
# print(z)

# exercise 2
'''
با کمک حلقه فور برنامه ای بنویس که پنج اسم را از ورودی دریافت نماید و داخل یک لیست ذخیره کند
اسم لیست:
names

'''

# names = []
# for i in range(5):
#     name = input(f'enter name number {i+1} ')
#     names.append(name)

# print(f'all names are : {names}')
# print('-----------------------------')
# print(f'{"id":<5}{"Student name":^20}')
# for i in range(len(names)):
#     print(f'{(i+1):<5}{names[i]:^20}')


# triangle


# p.forward(100)
# p.left(120)
# p.forward(100)
# p.left(120)
# p.forward(100)
# p.left(120)

# drawing triangle with for loop and turtle
# p.begin_fill()
# p.fillcolor('silver')
# for i in range(3):
#     p.forward(100)
#     p.left(120)
# p.end_fill()

# execise 3 : fill square with red color   مربع را با رنگ قرمز پر کن
# for i in range(4):
#     p.forward(100)
#     p.left(90)


# for i in range(5):
#     p.forward(100)
#     p.left(72)


# کشیدن ستاره
# p.clear()
# p.penup()
# p.setpos(-90, 30)
# p.pendown()

# for i in range(5):
#     p.forward(100)
#     p.right(144)
# p.shape('turtle')
# p.setpos(-50, 0)
# for i in range(3):
#     p.forward(100)
#     p.lt(120)

# p.begin_fill()
# p.fillcolor('yellow')

# for i in range(3):
#     p.forward(100)
#     p.right(120)
# p.end_fill()


# p.penup()
# p.setpos(-210, 150)
# p.pendown()
# p.write("This is my nice drawing project", font=("Arial", 20, "bold"))
# p.ht()


# drawing animation clock
import turtle
s = turtle.Screen()
s.bgcolor('orange')
s.setup(620, 620)
p = turtle.Pen()
p.pencolor('red')
p.pensize(4)
p.shape('turtle')
p.speed('normal')
for i in range(12):  # i = 2
    p.penup()
    p.seth(-30 * i + 60)
    p.forward(150)
    p.pendown()
    p.forward(25)
    p.penup()
    p.forward(20)
    p.write(i+1, font=('', 12, 'normal'))
    p.home()
p.penup()
p.goto(0, -240)
p.pendown()
p.circle(240)
p.penup()

p.setposition(-120, 250)
p.write("Our nice Animation clock", font=('Arial', 16, 'bold'))
# p.ht()
p.home()

s.exitonclick()
