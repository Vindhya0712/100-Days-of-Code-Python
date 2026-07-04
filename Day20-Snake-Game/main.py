from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Vindhya's Snake Game")
# Turn off default animations associated with the turtle
screen.tracer(0)

snake = Snake()
screen.update()

screen.listen()
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)


game_is_on = True
while game_is_on:
    # To skip appearance of movement of all three turtles separately
    screen.update()
    # To make animation feel more realistic
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()
