"""
In this program what we do is simply a turtle tries to cross a busy road
Requirements - Randomly generate cars
            - When the turtle completes one level the cars in next level is faster

Steps:
1. Set up the screen - Done
2. Set up the turtle behaviour - Done
3. Set up the cars - Done
4. Detect turtle collision with cars (Game over) - Done
5. Keep level
6. Speed up the cars when level goes up
"""

import turtle
from time import sleep
from player import Player
from cars import Cars
from level import Level

turtle.colormode(255)
# Setting up the screen
screen = turtle.Screen()
screen.title('The Turtle Crossing')
screen.setup(600, 600)

player = Player()
cars = Cars()
level = Level()

screen.tracer(0)
# Setting up the keys
screen.listen()
screen.onkeypress(player.up, 'Up')

game_continue = True

# Game loop
while game_continue:
    player.speed('normal')
    sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()
    # detecting collision
    for i in cars.cars:
        if i.distance(player) < 27:
            game_continue = False

    # detecting level up
    if player.ycor() >= 290:
        player.speed('fastest')
        player.goto(0, -290)
        cars.move_speed += 1
        level.level += 1
        level.update()

screen.exitonclick()