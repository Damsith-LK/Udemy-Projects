from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('white')
        self.speed('fastest')
        self.goto(0, 265)
        self.ht()
        self.color('black')
        self.write(arg=f"Level: {self.level}", move=False, align='center', font=('Ariel', 20, 'bold'))
