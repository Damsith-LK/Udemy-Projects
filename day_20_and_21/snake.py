# Import this on game.py

import turtle


class Snake:
    def __init__(self):
        self.snake = turtle.Turtle(shape='square')
        self.snake.color('white')
        self.snake.penup()
        self.snake.shapesize(stretch_wid=1, stretch_len=3)

    def move(self):
        self.snake.forward(20)

    def up(self):
        if self.snake.heading() != 270:
            self.snake.setheading(90)

    def down(self):
        if self.snake.heading() != 90:
            self.snake.setheading(270)

    def right(self):
        if self.snake.heading() != 180:
            self.snake.setheading(0)

    def left(self):
        if self.snake.heading() != 0:
            self.snake.setheading(180)
