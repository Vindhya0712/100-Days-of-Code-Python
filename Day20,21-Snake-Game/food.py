from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """Creates a food object and initializes essential attributes"""
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()


    def refresh(self):
        """Moves the food object to a new location"""
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(x=random_x, y=random_y)
