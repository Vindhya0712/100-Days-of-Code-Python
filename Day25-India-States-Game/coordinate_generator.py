import turtle

screen = turtle.Screen()

screen.setup(800, 800)
screen.bgpic('blank_india_map.gif')

turtle = turtle.Turtle()
turtle.shape('circle')
turtle.color('black')
turtle.penup()


def click(x, y):
    turtle.goto(x, y)
    user_input = screen.textinput(prompt='State name', title='Guess the state')
    turtle.write(arg=user_input, align='center')
    #turtle.write(f"{int(x)}, {int(y)}", align='left')
    print(int(x), int(y))


screen.onscreenclick(click)
screen.mainloop()