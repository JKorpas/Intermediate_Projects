from turtle import Turtle



class Palette(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
    def create_paddle(self, position):
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(position)


    def move_up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)

