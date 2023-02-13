# Here we are going to make a snake game (like the one in nokia) using turtle module
"""
Here are the steps:
1. Create the snake (The snake is 3 squares when starting) - Done
2. Move the snake - Done
3. Control the snake (Using event listeners) - Done
4. Detect collision with food - Done
5. Scoreboard - Done
6. Detect collision with wall (game over) - Done
7. Detect collision with tail (game over) - Done
8. Extend the snake - Done
"""

import turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from time import sleep

turtle.colormode(255)
screen = turtle.Screen()
screen.title('Snake Game')
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=1000, height=700)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_continue = True

while game_continue:
    scoreboard.display_score()
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        game_continue = False
        scoreboard.game_over()

    # Detect collision with tail
    for i in snake.segments:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 10:
            game_continue = False
            scoreboard.game_over()


screen.exitonclick()