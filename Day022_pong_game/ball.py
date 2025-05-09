from turtle import Turtle

TOP_EDGE = 280

class Ball (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move_count = 10
        self.y_move_count = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move_count
        new_y = self.ycor() + self.y_move_count
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move_count *= -1 #To reverse y direction

    def bounce_x(self):
        self.x_move_count *= -1 #To reverse x direction
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()