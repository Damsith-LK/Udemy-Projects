# Import this on game.py

import turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
turtle.colormode(225)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.create_segments(position)
    # These two methods create the snake body

    def create_segments(self, pos):
        new_seg = turtle.Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        self.create_segments(self.segments[-1].position())

    def move(self):
        for n_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[n_seg - 1].xcor()
            new_y = self.segments[n_seg - 1].ycor()
            self.segments[n_seg].goto(new_x, new_y)
        self.head.color((200, 200, 200))
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
