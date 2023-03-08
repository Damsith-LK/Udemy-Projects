from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt', 'r', encoding='utf-8') as data:
            self.highest_score = int(data.read())
        self.score = 0
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(x=0, y=310)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()

    def update_score_for_special_fruit(self):
        self.score += 6
        self.clear()

    def display_score(self):
        self.write(arg=f'Score: {self.score}  Highest Score: {self.highest_score}', move=False, align='center', font=('Ariel', 25, 'bold'))

    def reset_highest_score(self):
        self.highest_score = self.score
        with open('data.txt', 'w', encoding='utf-8') as data:
            data.write(str(self.highest_score))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER. YO DUMMY', move=False, align='center', font=('Times New Roman', 35, 'bold'))
