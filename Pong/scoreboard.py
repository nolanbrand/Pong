from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-80, 200)
        self.write(self.l_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(80, 200)
        self.write(self.r_score, align='center', font=('Courier', 50, 'normal'))

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1
