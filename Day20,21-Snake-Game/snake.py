from ctypes.wintypes import SMALL_RECT
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Initialize a snake object and get hold of the snake itself and its head"""
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]


    def create_snake(self):
        """Creates a snake with a default length of 60 pixels"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, pos):
        """Adds segments to the snake body"""
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(pos)
        self.snake_segment.append(new_segment)

    def extend(self):
        """Extends the snake body by one segment after every piece of food is eaten."""
        self.add_segment(self.snake_segment[-1].position())


    def move_snake(self):
        """Get the snake to move around on the screen"""
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg_num - 1].xcor()
            new_y = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(x=new_x, y=new_y)
        self.snake_segment[0].forward(MOVE_DISTANCE)


    def move_up(self):
        """Move snake in North direction. If snake is facing South, then it can't move North"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def move_down(self):
        """Move snake in South direction. If snake is facing North, then it can't move South"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def move_left(self):
        """Move snake in West direction. If snake is facing East, then it can't move West"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def move_right(self):
        """Move snake in East direction. If snake is facing West, then it can't move East"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
