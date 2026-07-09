from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level = 1
        self.update_level()


    def update_level(self):
        self.clear()
        self.goto(-270, 260)
        self.write(arg=f'Level: {self.level}', align='left', font=FONT)


    def game_over_message(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align='center', font=FONT)
        self.goto(0, -50)
        self.write(arg=f'Max Level: {self.level}', align='center', font=FONT)
