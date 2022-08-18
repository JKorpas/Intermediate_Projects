from turtle import Turtle
import random
COLORS = ["red", 'yellow', "blue","purple","orange","green"]
SPEED = 10
DESTINATION = 180
FREQUENCY = 6

class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = SPEED
        self.frequency = 6
    def create_car(self):
        random_choice = random.randint(1,3)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.choice(range(-250,270,10))
            new_car.goto(300, random_y)
            new_car.setheading(DESTINATION)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)
    def speed_up(self):
        self.speed +=5