from turtle import Turtle, Screen
from palette import Palette
from halfline import Halfline
from scoreboard import Scoreboard
from ball import Ball
import time

# Game Setup
# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# Animation Off
screen.tracer(0)
# Games items
# Ball
ball = Ball()
ball.create_ball()
# Scoreboards
score_player_left = Scoreboard((-200, 270))
score_player_right = Scoreboard((200, 270))
score_player_left.show_score()
score_player_right.show_score()
# Palettew
left_player = Palette((-350, 0))
right_player = Palette((350, 0))
# Halfline
halfline = Halfline()
halfline.draw()
# Show everything
screen.update()

screen.listen()
screen.onkeypress(left_player.move_up, "w")
screen.onkeypress(left_player.move_down, "s")
screen.onkeypress(right_player.move_up, "Up")
screen.onkeypress(right_player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.movement()
    # Collision with up/down border
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Collision with paddle
    if ball.distance(right_player) < 50 and ball.xcor() > 330 or ball.distance(left_player) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # Player Misses / Scoring points
    elif ball.xcor() > 390:
        score_player_left.update_score()
        ball.reset_ball()
    elif ball.xcor() < -390:
        score_player_right.update_score()
        ball.reset_ball()


screen.exitonclick()
