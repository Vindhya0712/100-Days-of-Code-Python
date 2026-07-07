from turtle import Turtle

MOVE_DISTANCE = 20
TOP_BOUNDARY = 250
BOTTOM_BOUNDARY = -250


class Paddle(Turtle):
    def __init__(self, pos_tuple):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=5)
        self.color('white')
        self.penup()
        self.setheading(90)
        self.goto(pos_tuple)


    def move_up(self):
        if self.ycor() < TOP_BOUNDARY:
            self.forward(MOVE_DISTANCE)


    def move_down(self):
        if self.ycor() > BOTTOM_BOUNDARY:
            self.backward(MOVE_DISTANCE)
