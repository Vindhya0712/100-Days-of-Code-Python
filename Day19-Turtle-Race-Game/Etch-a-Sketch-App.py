import turtle as t

vin = t.Turtle()


def move_fwd():
    vin.forward(10)


def move_bckwd():
    vin.backward(10)


def turn_left():
    new_heading = vin.heading() + 10
    vin.setheading(new_heading)


def turn_right():
    vin.right(10)


def clear_screen():
    vin.reset()


screen = t.Screen()
screen.listen()

screen.onkey(key='w', fun=move_fwd)
screen.onkey(key='s', fun=move_bckwd)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
