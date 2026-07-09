from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FINISH_MARGIN = 15


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.reached_finish = False


    def move(self):
        if self.ycor() < FINISH_LINE_Y - FINISH_MARGIN:
            self.forward(MOVE_DISTANCE)
        else:
            self.reached_finish = True

    def reset_position(self):
        if self.reached_finish:
            self.goto(STARTING_POSITION)
            self.reached_finish = False


