from turtle import Turtle


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
        self.forward(20)


    def move_down(self):
        self.backward(20)
