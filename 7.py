# turtle document:
# https://docs.python.org/3/library/turtle.html
# convert to gif:
# https://cloudconvert.com/png-to-gif

# remove background
# https://www.remove.bg/

import turtle

s = turtle.Screen()
s.title("my app")
s.bgcolor('orange')
s.bgpic('mario.png')
# s.register_shape('my_shape', ((10, 0), (10, 10), (0, 10), (0, 0)))
s.register_shape("strawberry.gif")
p = turtle.Pen()
# p.shape('my_shape')
p.shape('strawberry.gif')
# p.shape('turtle')  # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
# p.setpos(200,200)
# p.forward(100)
# p.fd(100)
# p.bk(100)
# p.back(100)
# p.backward(100)
p.pencolor("red")
p.pensize(4)
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


p.setheading(45)  # p.seth(45)
p.forward(200)
s.exitonclick()
print("END")


# excersise1
'''
مثلث
پنجضلعی
شش ضلعی
وستاره


'''
