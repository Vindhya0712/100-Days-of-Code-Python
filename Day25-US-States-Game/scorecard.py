from turtle import Turtle


FONT = ('Arial', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=250)
        self.color('black')
        self.score = 0


    def update_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score}/50', align='center', font=FONT)