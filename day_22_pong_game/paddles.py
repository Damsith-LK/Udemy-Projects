from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.shape('square')
        self.speed('fastest')
        self.goto(x, y=0)
        self.right(90)
        self.color('white')
        self.speed('normal')

    def up(self):
        self.backward(20)

    def down(self):
        self.forward(20)