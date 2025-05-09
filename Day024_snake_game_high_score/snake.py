from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20 , 0), (-40, 0)]
STEPS_COUNT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_coord = self.segments[seg_num - 1].xcor()
            new_y_coord = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_coord, new_y_coord)
        self.head.forward(STEPS_COUNT)


    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.head.heading() != DOWN: # can only go up when not currently going down
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if  self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if  self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]