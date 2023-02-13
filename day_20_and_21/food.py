from turtle import Turtle
from random import randint
from time import process_time


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('yellow')
        self.speed('fastest')
        self.goto(x=randint(-480, 480), y=randint(-330, 330))
        self.new_food()

    def new_food(self):  # When the snake collides with the food
        rand_x = randint(-480, 480)
        rand_y = randint(-330, 330)
        self.goto(rand_x, rand_y)


class SpecialFood(Turtle):

    def __init__(self):
        super().__init__()

    def special_food(self):
        self.penup()
        self.speed('fastest')
        self.shape('turtle')
        self.color('red')
        rand_x = randint(-480, 480)
        rand_y = randint(-330, 330)
        self.goto(rand_x, rand_y)
        if process_time() >= 6:
            self.goto(700, 700)