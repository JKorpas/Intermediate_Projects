from turtle import Turtle
START = (0,-280)
SPEED = 20
DESTINATION = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()
        self.move = SPEED
    def create_turtle(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(START)
        self.setheading(DESTINATION)
    def move_up(self):
        self.forward(self.move)

    def reach_finish(self):
        self.goto(START)

        
