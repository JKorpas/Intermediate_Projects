from turtle import Turtle, Screen, colormode
import random

#screen setup
screen = Screen()
screen.setup(width=700, height=500, startx=0, starty=0)


def randomize_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

#Creating tutrles objects
names = ["franklin", "leonardo", "donatello", "michelangelo", "raphael"]
colors = ["red", "black", "blue", "yellow", "green", "purple"]
turtles = [Turtle() for name in names]
#User bet
user_bet = screen.textinput("Try to guess winner", f"{' '.join(colors[:len(names)]).title()}").title()
if user_bet:
    is_race_on = True

#Calculating distance depending on number of turtles
end_distance = (screen.window_width()-50)/2
distance_to_start_on_x_axis = -(screen.window_width()/2) + 10
distance_to_separate = screen.window_height()/ len(turtles)
distance_to_start_on_y_axis = -((screen.window_height()-distance_to_separate)/2)

#Adding and setting turtles on proper position 
colormode(255)
for turtle, color in zip(turtles,colors):
    turtle.penup()
    turtle.goto(distance_to_start_on_x_axis, distance_to_start_on_y_axis)
    turtle.shape("turtle")
    turtle.color(color)
    distance_to_start_on_y_axis += distance_to_separate
    


#Randomize movemnt
def go_forward(obj):
    obj.forward(random.choice(range(4, 21, 2)))

# main loop
while is_race_on:
    for turtle in turtles:
        go_forward(turtle)
        if turtle.xcor() >= end_distance:
            print(f"{turtle.pencolor().title()} Wins")
            if turtle.pencolor().title() == user_bet:
                print(f"Winner, You guessed right! Winner is {turtle.pencolor().title()}")
            else:
                print(f"Looser, You guessed wrong! Winner is {turtle.pencolor().title()}, Your guess was {user_bet}")
            is_race_on = False
            break

screen.exitonclick()

"""Sketch app 
def move_forward():
    self.forward(15)

def move_backward():
    self.backward(15)

def clockwise():
    self.right(8)

def otherwise_clockwise():
    self.left(8)

def clear_screen():
    self.penup()
    self.home()
    self.clear()
    self.pendown()"""
    
''' 
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=otherwise_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()  '''


