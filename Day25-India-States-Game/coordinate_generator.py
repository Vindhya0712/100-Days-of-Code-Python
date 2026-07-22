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
    turtle.write(arg=user_input.title(), align='center', font=('Arial', 10, 'bold'))
    print(f"{user_input}, {int(x)}, {int(y)}")


screen.onscreenclick(click)
screen.mainloop()
