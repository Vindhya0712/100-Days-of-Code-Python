import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "DarkOrange", "VioletRed2"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LANES = [-250, -220, -190, -160, -130, -100, -70, -40, -10, 20, 50, 80, 110, 140, 170, 200, 230, 245]


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        spawn_car = random.randint(1, 6)
        if spawn_car == 1:
            car = Turtle(shape='square')
            car.shapesize(stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(x=250, y=random.choice(LANES))
            self.cars.append(car)


    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.car_speed)


    def car_left_screen(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.color(random.choice(COLORS))
                car.goto(x=300, y=random.randint(-250, 250))


    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
