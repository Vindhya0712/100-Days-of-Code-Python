from turtle import Turtle


FONT = ('Arial', 10, 'bold')


class TurtleWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 0)
        self.penup()
        self.color('black')
        self.ut = ['Delhi', 'Andaman And Nicobar Islands', 'Lakshadweep', 'Daman And Diu', 'Ladakh', 'Jammu And Kashmir',
                   'Chandigarh', 'Puducherry']


    def write_state_name(self, xpos, ypos, state_name):
        self.goto(x=xpos, y=ypos)
        state_name = state_name.title()
        if state_name in self.ut:
            self.color('red')
            self.write(arg=state_name, align='center', font=FONT)
            self.color('black')
        else:
            self.write(arg=state_name, align='center', font=FONT)
