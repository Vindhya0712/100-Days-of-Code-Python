from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Initialize a snake object with default length of 60 pixels"""
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]


    def create_snake(self):
        for segment in range(3):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(x=(0 - 20 * segment), y=0)
            self.snake_segment.append(new_segment)


    def move_snake(self):
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg_num - 1].xcor()
            new_y = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(x=new_x, y=new_y)
        self.snake_segment[0].forward(MOVE_DISTANCE)


    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
