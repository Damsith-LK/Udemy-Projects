"""
Here are the steps:
1. Setup the two paddles in the either sides of the game window - Done
2. Setup the ball movement - Done
3. Setup the line in the middle
4. Detect collisions with paddles - Done
5. Detect when the ball misses the paddle - Done
6. Keeping the score
7. Changing ball speed
"""

import turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = turtle.Screen()
screen.title('The Pong Game')
screen.bgcolor('black')
screen.setup(width=1000, height=700)

# Setting up the paddles
left_paddle = Paddle(-490)
right_paddle = Paddle(480)

# Listening
screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

# Setting up the line between
line = turtle.Turtle()
line.speed('fastest')
line.goto(0, 360)
line.right(90)
line.pencolor('white')
for _ in range(20):
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()

ball = Ball()
scoreboard = Scoreboard()
game_continue = True

# Game loop
while game_continue:
    sleep(0.1)
    scoreboard.display_score()
    screen.update()
    ball.move()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    # Detecting collision with right paddle
    if ball.xcor() > 450 and right_paddle.distance(ball) < 90:
        ball.bounce_x()
    # Missing the right paddle
    elif ball.xcor() > 460:
        scoreboard.left_score += 1
        scoreboard.update_score()
        ball.speed('fastest')
        ball.goto(0, 0)
        sleep(3)

    # Detecting the collision with left paddle
    if ball.xcor() < -460 and left_paddle.distance(ball) < 90:
        ball.bounce_x()
    # Missing the left paddle
    elif ball.xcor() < -460:
        scoreboard.right_score += 1
        scoreboard.update_score()
        ball.speed('fastest')
        ball.goto(0, 0)
        sleep(3)

screen.exitonclick()