from turtle import Screen, Turtle

window = Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)

snake_head = Turtle()
snake_head.shape("square")
snake_head.color("black")
snake_head.speed("fastest")
snake_head.penup()

while True:
    window.update()
