from turtle import Turtle
import time


SPAWN_X = 0
SPAWN_Y = 0
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.segments.extend([Turtle() for i in range(3)])
        global SPAWN_X
        global SPAWN_Y
        for s in self.segments:
            s.penup()
            s.color("white")
            s.shape("square")
            s.goto(SPAWN_X, SPAWN_Y)
            SPAWN_X -= 20

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        time.sleep(0.1)
        for s in range(len(self.segments)-1, 0, -1):
            self.segments[s].goto(self.segments[s-1].position())
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        # self.head.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        # self.head.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        # self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        # self.head.forward(MOVE_DISTANCE)
