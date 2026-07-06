from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.title("Vindhya's Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
screen.update()

screen.listen()
screen.onkey(key='Up', fun=right_paddle.move_up)
screen.onkey(key='Down', fun=right_paddle.move_down)
screen.onkey(key='w', fun=left_paddle.move_up)
screen.onkey(key='s', fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
