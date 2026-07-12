from turtle import Turtle


FONT = ('Arial', 8, 'normal')


class TurtleWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 0)
        self.penup()
        self.color('black')


    def write_state_name(self, xpos, ypos, state_name):
        self.goto(x=xpos, y=ypos)
        self.write(arg=state_name, align='center', font=FONT)