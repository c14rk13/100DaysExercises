import random
from turtle import Turtle, Screen

starting_pos = -230
finish_line = 230
y_position = 175
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_racers = []
is_race_on = False

def create_turtle(color, y_pos):
    trtl =  Turtle()
    trtl.color(color)
    trtl.shape("turtle")
    #trtl.shapesize(2)
    trtl.penup()
    trtl.setposition(starting_pos, y_pos)
    return  trtl


def check_winner(color_bet, winning_color):
    if color_bet == winning_color:
        print(f"You win! The {winning_color} wins")
    else:
        print(f"You lose! The {winning_color} wins")



screen = Screen()
screen.setup(500, 450)

user_bet = screen.textinput(title="Turtle Race bet", prompt="What color is your bet?").lower()

for turtle_idx in range(0, 6):
    turtle_racers.append(create_turtle(colors[turtle_idx], y_position))
    y_position -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_racers:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= finish_line:
            is_race_on = False
            check_winner(user_bet, turtle.pencolor())


screen.exitonclick()