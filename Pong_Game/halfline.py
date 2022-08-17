from turtle import Turtle

HALF_WIDTH = 290

class Halfline(Turtle):
    def __init__(self):
        super().__init__()
    def draw(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -HALF_WIDTH)
        self.width(20)
        self.pendown()
        self.goto(0, HALF_WIDTH)