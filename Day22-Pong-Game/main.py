from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.title("Vindhya's Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
screen.update()

screen.listen()
screen.onkey(key='Up', fun=right_paddle.move_up)
screen.onkey(key='Down', fun=right_paddle.move_down)
screen.onkey(key='w', fun=left_paddle.move_up)
screen.onkey(key='s', fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce
        ball.bounce_y()

    # Detect collision with both paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        print('Made contact')
        ball.bounce_x()

    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        print('Made contact')
        ball.bounce_x()



screen.exitonclick()
