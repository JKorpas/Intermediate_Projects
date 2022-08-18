from turtle import Turtle

ALIGMENT = "center"
FONT = ('Arial', 18, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0 
        self.goto(0, 270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.read_highscore_from_file()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def update_score(self):
        self.score += 1

        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore_to_file()
        self.score = 0
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def save_highscore_to_file(self):
        with open("HighScore.txt", "w+") as file:
            file.write(f'{self.high_score}')

    def read_highscore_from_file(self):
        with open("HighScore.txt", "r+") as file:
            self.high_score = int(file.read())
            return self.high_score