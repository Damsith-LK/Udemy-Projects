# Here we are going to make a snake game (like the one in nokia) using turtle module
"""
Here are the steps:
1. Create the snake (The snake is 3 squares when starting) - Done
2. Move the snake - Done
3. Control the snake (Using event listeners) - Done
4. Detect collision with food - Done
5. Scoreboard
6. Detect collision with wall (game over)
7. Detect collision with tail (game over)
"""

import turtle
from snake import Snake
from food import Food
from time import sleep

screen = turtle.Screen()
screen.title('Snake Game')
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=1000, height=700)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_continue = True

while game_continue:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()


screen.exitonclick()