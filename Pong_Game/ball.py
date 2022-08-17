from pydoc import plain
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.y_move = 5
        self.x_move = 5
    def create_ball(self):
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0, 0)
        
    def movement(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= 1.1
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = 5
        self.bounce_x()
        