from turtle import Turtle

STEP_DISTANCE = 20
TOP_EDGE = 240
BOTTOM_EDGE = -240

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + STEP_DISTANCE
        if self.ycor() < TOP_EDGE:
            self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - STEP_DISTANCE
        if self.ycor() > BOTTOM_EDGE:
            self.goto(self.xcor(), new_y)