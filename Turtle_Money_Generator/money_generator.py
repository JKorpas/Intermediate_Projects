import fractions
from turtle import Screen, Turtle, colormode
import random
import colorgram


def randomize_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#couple fucntion to warm-up
# Drawing all shapes from triangle dosn't need loop
def draw_shapes(shapes):
    for i in range(3, shapes):
        franklin.pencolor(randomize_color())
        turn = 180 - ((shapes - 2) * 180 / shapes)
        for j in range(i):
            franklin.forward(100)
            franklin.right(turn)

# drawing shape by shape need loop to operate
def draw_shape(shape):
    franklin.pencolor(randomize_color())
    turn = 180 - ((shape - 2) * 180 / shape)
    for _ in range(shape):
        franklin.forward(100)
        franklin.right(turn)


def random_walk():
    franklin.speed(10)
    franklin.pensize(16)
    franklin.pencolor(randomize_color())
    franklin.setheading(random.choice([0, 90, 180, 270]))
    franklin.forward(30)


def draw_spirograph(circles, size):
    franklin.speed(16)
    franklin.pensize(1)
    turn = 360 / circles
    for _ in range(circles):
        franklin.circle(size)
        franklin.pencolor(randomize_color())
        franklin.right(turn)

#main function 


franklin = Turtle()
franklin.shape("turtle")
franklin.color("black")
colormode(255)


franklin.penup()
franklin.dot()
franklin.forward(100)
franklin.dot()
franklin.right(90)
franklin.forward(100)
franklin.dot()

screen = Screen()
screen.setup(800,600)
screen.exitonclick()
