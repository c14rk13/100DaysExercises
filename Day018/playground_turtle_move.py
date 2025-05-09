from turtle import Turtle, Screen
# from turtle import *
# import turtle as t
import heroes


the_turtle = Turtle()

# Turtle appearance
the_turtle.color("steel blue")
the_turtle.shape("circle")
the_turtle.pensize(5)

# Draw a square
for i in range(4):
    the_turtle.forward(100)
    the_turtle.left(90)


# Pen up, then position pen below the square
the_turtle.penup()
#the_turtle.right(90)
#the_turtle.forward(20)
#the_turtle.left(90)
the_turtle.setpos(-400, 400)
the_turtle.color("light coral") # Let's use a different color this time
the_turtle.pensize(2)

for i in range(50):
    the_turtle.pendown()
    the_turtle.forward(5)
    the_turtle.penup()
    the_turtle.forward(5)


screen = Screen()
screen.exitonclick()

