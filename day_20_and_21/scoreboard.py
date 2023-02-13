from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(x=0, y=310)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()

    def display_score(self):
        self.write(arg=f'Score: {self.score}', move=False, align='center', font=('Ariel', 25, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER. YO DUMMY', move=False, align='center', font=('Times New Roman', 35, 'bold'))
