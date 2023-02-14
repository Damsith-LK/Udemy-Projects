from turtle import Turtle
from random import randint


class Cars(Turtle):

    def __init__(self):
        self.level = 1
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape('square')
        self.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(280, randint(-280, 280))

    def move(self):
        self.backward(20)
