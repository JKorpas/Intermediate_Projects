from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager
import time
import random
# Setup Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
# Items
player = Player()
score = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
screen.update()

while game_is_on:
    time.sleep(0.09)
    car_manager.create_car()
    screen.update()
    score.show_level()
    car_manager.move_cars()
    if score.level % 6 == 0 and score.frequency > 2:
        score.frequency -= 1
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            screen.update()
            score.game_over()
            game_is_on = False
    if player.ycor() >= 280:
        player.reach_finish()
        score.update_score()
        car_manager.speed_up()

screen.exitonclick()
