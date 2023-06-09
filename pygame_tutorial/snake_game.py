from turtle import Screen, Turtle
from random import randint
from time import sleep


def generate_turtle_object(shape, color):
    turtle_object = Turtle()
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.speed("fastest")
    turtle_object.penup()
    return turtle_object


def change_food_position():
    food_x = randint(-270, 270)
    food_y = randint(-270, 270)
    food.goto(food_x, food_y)


def move_snake():
    if snake_head.direction == "up":
        yposition = snake_head.ycor()
        snake_head.sety(yposition + 20)
    if snake_head.direction == "down":
        yposition = snake_head.ycor()
        snake_head.sety(yposition - 20)
    if snake_head.direction == "left":
        xposition = snake_head.xcor()
        snake_head.setx(xposition - 20)
    if snake_head.direction == "right":
        xposition = snake_head.xcor()
        snake_head.setx(xposition + 20)


def change_dir_to_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def change_dir_to_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def change_dir_to_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def change_dir_to_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def reset():
    snake_head.goto(0, 0)
    snake_head.direction = ""
    # TODO hide bodies and clear snake_body list


window = Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)

snake_head = generate_turtle_object("square", "black")
snake_head.direction = ""
window.listen()
window.onkeypress(change_dir_to_up, "Up")
window.onkeypress(change_dir_to_left, "Left")
window.onkeypress(change_dir_to_right, "Right")
window.onkeypress(change_dir_to_down, "Down")


food = generate_turtle_object("circle", "red")
change_food_position()

snake_body = []
while True:
    window.update()
    if snake_head.distance(food) < 20:
        change_food_position()
        new_body = generate_turtle_object("square", "grey")
        snake_body.append(new_body)

    for i in range(len(snake_body) - 1, 0, -1):
        prev_x = snake_body[i-1].xcor()
        prev_y = snake_body[i-1].ycor()
        snake_body[i].goto(prev_x, prev_y)

    if len(snake_body) > 0:
        head_x = snake_head.xcor()
        head_y = snake_head.ycor()
        snake_body[0].goto(head_x, head_y)

    if snake_head.xcor() > 290:
        reset()

    move_snake()
    sleep(0.2)
