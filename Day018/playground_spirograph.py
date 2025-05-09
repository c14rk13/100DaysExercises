from turtle import Turtle, Screen, colormode
import random

trtl = Turtle()


def random_color():
    r = random.randint(150, 250)
    g = random.randint(150, 250)
    b = random.randint(150, 250)

    color = (r, g, b)
    return color


def draw_spirograph(gap_size):
    radius = 100
    heading = 0

    for heading in range(0, 360, gap_size):
        trtl.pencolor(random_color())
        trtl.circle(100)
        trtl.setheading(heading)


trtl.shape("circle")
trtl.pensize(2)
trtl.color("slate gray")
trtl.speed("fastest")
colormode(255)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()