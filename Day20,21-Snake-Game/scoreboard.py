from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        """Creates a scorecard object and initializes essential attributes"""
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.pencolor('white')
        self.print_score()


    def print_score(self):
        """Updates score and prints it onto the Turtle Graphics Window"""
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)


    def end_game_msg(self):
        """Prints the end of game message"""
        self.goto(0, 0)
        self.write('GAME OVER.', align=ALIGNMENT, font=FONT)


