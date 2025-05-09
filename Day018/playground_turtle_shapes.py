import turtle
from turtle import Turtle, Screen, colormode
import random

trtl = Turtle()

# Start at mid-top
# Draw a triangle, then square, then pentagon, etc
# start with 3 sides, increasing # of sides
# Each completed shape in random color

def draw(sides):
    angle = 360 / sides

    for i in range(sides):
        trtl.forward(100)
        trtl.right(angle)

trtl.shape("circle")
trtl.teleport(None, 350)

for shape_sides in range(3, 12):
    # randomize the color -- rgb 0 - 255 but I only want pastel colors
    r_color = random.randrange(150, 250)
    g_color = random.randrange(150, 250)
    b_color = random.randrange(150, 250)
    colormode(255)
    trtl.pencolor(r_color, g_color, b_color)
    trtl.fillcolor(r_color, g_color, b_color)
    trtl.filling()

    draw(shape_sides)


screen = Screen()
screen.exitonclick()