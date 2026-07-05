from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Vindhya's Snake Game")
# Turn off default animations associated with the turtle
screen.tracer(0)

# Creates a snake with default length currently being 60 pixels long
snake = Snake()
# Creates food on the screen
food = Food()
scorecard = Scoreboard()
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
    # Detect collision with food
    if snake.head.distance(x=food, y=None) < 15:
        scorecard.score += 1
        scorecard.print_score()
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scorecard.end_game_msg()

    # Detect collision with tail
    for segment in snake.snake_segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scorecard.end_game_msg()


screen.exitonclick()
print(f"Well played! \nYour final score: {scorecard.score} \nThanks for playing!")
