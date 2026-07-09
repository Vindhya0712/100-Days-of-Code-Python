import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Vindhya's Turtle Crossing Game 🐢")
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.create_cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    car_manager.car_left_screen()
    if player.reached_finish:
        player.reset_position()
        scoreboard.level += 1
        scoreboard.update_level()
        car_manager.increase_car_speed()

    for car in car_manager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over_message()
            game_is_on = False
            print(f"Max level reached: {scoreboard.level}")


screen.exitonclick()
