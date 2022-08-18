from turtle import Turtle


ALIGMENT = "center"
FONT = ('Arial', 18, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-320, 250)

    def show_level(self):
        self.color("Black")
        self.write(f"Level: {self.level}", False, align=ALIGMENT, font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.show_level()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("Black")
        self.write(
            f"Game Over on level: {self.level}", False, align=ALIGMENT, font=FONT)
