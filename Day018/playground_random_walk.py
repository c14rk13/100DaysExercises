from turtle import Turtle, Screen, colormode
import random

trtl = Turtle()

# start at home() position (or does it also need to be random?)
# LOOP: make 1 turn left/right/not, then move forward 1 step
# Does it need to check for screen boundaries (ex. position x or y should not exceed |350|)
# choose diff color for each step
# Make the drawing faster (no delay)

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(150, 250)
    g = random.randint(150, 250)
    b = random.randint(150, 250)

    random_color = (r, g, b)
    return random_color



trtl.shape("circle")
trtl.pensize(5)
trtl.color("slate gray")
trtl.speed("fast")
colormode(255)

for _ in range(100):
    # randomize the color -- rgb 0 - 255, but I only want pastel colors
    trtl.pencolor(random_color())

    trtl.setheading(random.choice(directions))
    trtl.forward(30)


screen = Screen()
screen.exitonclick()