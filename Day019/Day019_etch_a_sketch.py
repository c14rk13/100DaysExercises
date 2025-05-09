from turtle import Turtle, Screen

turtago = Turtle()
board = Screen()


# W - move forward
# S - turn backwards
# A - counterclockwise
# D - clockwise
# C - clear drawing

def clear_drawing():
    turtago.reset()


def move_forwards():
    turtago.forward(10)

def turn_backwards():
    turtago.backward(10)

def turn_clockwise():
    turtago.right(10)


def turn_counter_clockwise():
    turtago.left(10)


board.listen()
board.onkey(key="c", fun=clear_drawing)
board.onkey(key="w", fun=move_forwards)
board.onkey(key="s", fun=turn_backwards)
board.onkey(key="a", fun=turn_clockwise)
board.onkey(key="d", fun=turn_counter_clockwise)

board.exitonclick()
