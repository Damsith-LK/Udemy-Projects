"""
Here are the steps:
1. Setup the two paddles in the either sides of the game window
2. Setup the ball movement
3. Setup the line in the middle
4. Detect collisions with paddles
5. Detect when the ball misses the paddle
6. Keeping the score
7. Changing ball speed
"""

import turtle
from paddles import Paddle
from ball import Ball
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

ball = Ball()
game_continue = True

# Game loop
while game_continue:
    sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 330:
        ball.bounce()

screen.exitonclick()