"""
In this program what we do is simply a turtle tries to cross a busy road
Requirements - Randomly generate cars
            - When the turtle completes one level the cars in next level is faster

Steps:
1. Set up the screen
2. Set up the turtle behaviour
3. Set up the cars
4. Level up when turtle reaches the other side
5. Speed up the cars when level goes up
6. Game over if turtle gets hit
"""

import turtle
from time import sleep
from player import Player
from cars import Cars

turtle.colormode(255)
# Setting up the screen
screen = turtle.Screen()
screen.title('The Turtle Crossing')
screen.setup(600, 600)
screen.tracer(2)

player = Player()

screen.tracer(1)
# Setting up the keys
screen.listen()
screen.onkeypress(player.up, 'Up')


game_continue = True
# Game loop
while game_continue:
    sleep(0.1)
    screen.update()
    car = Cars()
    car.move()


screen.exitonclick()