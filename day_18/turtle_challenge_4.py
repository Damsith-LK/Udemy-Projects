"""
New things to do:

1. Get a larger pensize
2. increase the speed of the turtle
"""

import turtle
from random import choice

colors = ['red', 'green', 'black', 'blue', 'navy', 'orange', 'gold', 'cyan', 'coral', 'yellow', 'violet', 'chartreuse']

my_turtle = turtle.Turtle()
my_turtle.pensize(9)
my_turtle.speed(10)

# Generating a random walk
directions = ['forward', 'left', 'right']
for _ in range(1000):
    rand_color = choice(colors)
    rand_dir = choice(directions)
    my_turtle.pencolor(rand_color)
    if rand_dir == 'forward':
        my_turtle.forward(20)
    elif rand_dir == 'right':
        my_turtle.right(90)
        my_turtle.forward(20)
    else:
        my_turtle.left(90)
        my_turtle.forward(20)


screen = turtle.Screen()
screen.exitonclick()