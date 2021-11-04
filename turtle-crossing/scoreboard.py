from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-270, y=260)
        self.update_score()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f'Level: {self.score}', align='left', font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write('GAME OVER', align='center', font=FONT)
