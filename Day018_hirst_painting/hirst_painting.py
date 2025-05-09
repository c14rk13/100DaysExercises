from turtle import Turtle, Screen, colormode
import random

trtl = Turtle()
trtl.hideturtle()
trtl.speed("fast")

colormode(255)
dot_size = 15
pace_size = 30
x_width = 10
y_height = 10
total_dots = x_width * y_height
x_coord = 0 - int(x_width * pace_size/2)
y_coord = x_coord

color_list = [(235, 239, 237), (233, 238, 241), (204, 149, 109), (13, 29, 84), (74, 99, 122),
              (130, 161, 190), (192, 131, 153), (65, 26, 7), (75, 107, 81), (124, 80, 54),
              (237, 217, 226), (184, 102, 121), (141, 11, 5), (70, 25, 50), (178, 140, 54),
              (106, 33, 55), (232, 199, 116), (30, 55, 108), (186, 182, 209)]


# draw 10x10 canvas of dots, equally spaced
#       - LOOP: pen down, draw dot, pen up, move 50 paces
#       - set x, y coordinates after every 10 dots; 10 dots at 20 size + 10 moves at 50 paces (10*20 + 10*9 = 600) -> div by 2


# draw a row of dots:
trtl.penup()
trtl.setposition(x_coord, y_coord)
for dot_count in range(1, total_dots + 1):
    trtl.dot(dot_size, random.choice(color_list))
    trtl.forward(pace_size)

    if dot_count % x_width == 0:
        y_coord += pace_size
        trtl.setposition(x_coord, y_coord)

screen = Screen()
screen.exitonclick()