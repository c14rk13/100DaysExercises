from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

# PONG Game:
# * Create the screen
# * Create and move a paddle
# * Create another paddle
# * Create the ball and make it move
# * Detect collision with the wall and bounce
# * Detect collision with paddle
# * Detect when paddle misses
# * Keep score


# Create Screen: W=800, H=600
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()
screen.listen()

# Left paddle
screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)


# Right paddle
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # bounce if ball hits the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bounce if the ball hits the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Lose score if ball goes past right/left edge
    # Left paddle misses, right paddle scores
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    # Left paddle misses, right paddle scores
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()



screen.exitonclick()

