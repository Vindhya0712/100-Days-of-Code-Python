from turtle import Turtle

FONT = ('Courier New', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.divide_screen()


    def update_score(self):
        self.clear()
        self.divide_screen()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=FONT)


    def divide_screen(self):
        self.color('white')
        self.shape('square')
        self.pensize(10)
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-300)
        for i in range(50):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
