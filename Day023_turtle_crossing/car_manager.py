import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

            # When a car reaches the end of the screen,
            # remove from the list to save resources
            if car.xcor() < -300:
                self.all_cars.remove(car)


    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT