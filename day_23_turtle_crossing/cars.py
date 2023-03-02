from turtle import Turtle
from random import randint, choice

COLORS = ['orange', 'yellow', 'cyan', 'blue', 'green', 'brown', 'red', 'purple', 'pink']


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_speed = 5
        self.color('white')

    def create_cars(self):
        rand = randint(1, 6)
        if rand == 1:
            new_car = Turtle()
            new_car.speed('fastest')
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-280, 280))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())