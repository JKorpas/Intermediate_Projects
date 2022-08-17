from turtle import Turtle

ALIGMENT = "center"
FONT = ('Arial', 18, 'bold')


class Scoreboard(Turtle):
    player = 1

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(position)

    def show_score(self):
        self.color("white")
        self.write(f"Score: {self.score}", False, align=ALIGMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()
        