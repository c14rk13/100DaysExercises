# Snake Game:
# 1. Create a snake body
# 2. Move the snake
# 3. Create Snake food
# 4. Detect Collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

from turtle import Screen
import time

from scoreboard import ScoreBoard
from snake import Snake
from food import Food


# For a 600 by 600 screen
SCREEN_SQUARE_EDGE_1 = -280
SCREEN_SQUARE_EDGE_2 = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game c14")
screen.tracer(0)    # Turn off tracer


# 1. Create a snake body (20x20 default dimension)
snake = Snake()

# Create food:
food = Food()

# Create Scoreboard:
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# 2. Move the snake; move from tail to head
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with  food (use turtle method - distance)
    # If snake and food collide -- food should go to another random position
    #       and add to snake tail
    if snake.head.distance(food) < 15: #Food is 10x10 circle, allow for overlap
        food.move()
        snake.extend()
        scoreboard.update_score() #Update and write score

    # Detect collision with Wall
    if (snake.head.xcor() > SCREEN_SQUARE_EDGE_2 or snake.head.xcor() < SCREEN_SQUARE_EDGE_1
            or snake.head.ycor() > SCREEN_SQUARE_EDGE_2 or snake.head.ycor() < SCREEN_SQUARE_EDGE_1):
        # game_is_on = False
        scoreboard.reset_scoreboard()
        snake.reset()


    #Detect collision with any segment in the tail
    for segment in snake.segments[1:]: #Slice the list to start at 2nd segment - Bypass/Ignore the snake.head distance to itself
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset_scoreboard()
            snake.reset()

screen.exitonclick()