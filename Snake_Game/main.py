
from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.update()

game = Snake()
food = Food()
score = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(game.move_up, "Up")
screen.onkey(game.move_down, "Down")
screen.onkey(game.move_left, "Left")
screen.onkey(game.move_right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    game.move()
    # Collision with fodd
    if game.head.distance(food) <= 10:
        food.refresh()
        game.extend_snake()
        score.update_score()
    # Collision with wall
    if game.head.xcor() > 380 or game.head.xcor() < -380 or game.head.ycor() > 290 or game.head.ycor() < -290:
        score.reset()
        game.reset()
    for segment in game.segments[1:]:
        if game.head.distance(segment) < 5:
            score.reset()
            game.reset()
screen.exitonclick()
