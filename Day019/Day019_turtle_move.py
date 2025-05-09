import turtle as Trtl

le_turtl = Trtl.Turtle()
screen = Trtl.Screen()


def move_forwards():
    le_turtl.forward(10)

def turtle_appearance():
    le_turtl.shape("turtle")
    le_turtl.shapesize(2)
    le_turtl.color("rosy brown")

turtle_appearance()
screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()