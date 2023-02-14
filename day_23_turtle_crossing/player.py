from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.speed(0)
        self.penup()
        self.left(90)
        self.goto(0, -290)

    def up(self):
        self.forward(20)