from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.goto(0, 240)
        self.hideturtle()

    def display_score(self):
        self.write(arg=f'{self.left_score}     {self.right_score}', align='center', move=False, font=('Courier', 80, 'normal'))

    def update_score(self):
        self.clear()
        self.write(arg=f'{self.left_score}     {self.right_score}', align='center', move=False, font=('Courier', 80, 'normal'))

    def win(self, side, name):
        self.goto(0, 0)
        self.write(f'The {side} side player {name} won!!!', align='center', move=False, font=('Times New Roman', 40, 'bold'))

    def draw(self):
        self.goto(0, 0)
        self.write(f"That's a goddamn draw!!!")