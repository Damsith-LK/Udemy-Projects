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

# The new feature special_food is pending but the difficulty modes seem to be good
# Also adding a **Highest score** thing - success

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
difficulty = screen.textinput('Choose your difficulty', 'What do you choose (easy or medium or hard or EXTREME or GOD').lower()
difficulties = {'easy': 0.2, 'medium': 0.097, 'hard': 0.07, 'extreme': 0.04, 'god': 0.01}

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
# special_food = SpecialFood()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_continue = True
if difficulty not in difficulties.keys():
    game_continue = False

while game_continue:
    scoreboard.display_score()
    screen.update()

    sleep(difficulties[difficulty])
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.update_score()

    # if scoreboard.score % 6 == 0:
    #     # special_food.special_food()
    #     if snake.head.distance(special_food) < 15:
    #         scoreboard.update_score_for_special_fruit()

    # Detect collision with wall
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        game_continue = False
        scoreboard.game_over()

    # Detect collision with tail
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_continue = False
            scoreboard.game_over()

    # Updating the high score
    if scoreboard.score > scoreboard.highest_score:
        scoreboard.reset_highest_score()


screen.exitonclick()