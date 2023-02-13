# Ball Width and height is both 20
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.shape('circle')
        self.penup()
        self.shapesize()
        self.speed('normal')
        self.x_speed = 10
        self.y_speed = 10

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_speed *= -1
