"""
New things to do:

1. Get a larger pensize
2. increase the speed of the turtle
"""

import turtle
from random import choice, randint

# colors = ['red', 'green', 'black', 'blue', 'navy', 'orange', 'gold', 'cyan', 'coral', 'yellow', 'violet', 'chartreuse']

my_turtle = turtle.Turtle()
my_turtle.pensize(9)
my_turtle.speed(10)
turtle.colormode(255)
# Generating a random walk
directions = ['forward', 'left', 'right']
for _ in range(1000):
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)

    rand_dir = choice(directions)
    my_turtle.pencolor((r, g, b))
    if rand_dir == 'forward':
        my_turtle.forward(20)
    elif rand_dir == 'right':
        my_turtle.right(90)
        my_turtle.forward(20)
    else:
        my_turtle.left(90)
        my_turtle.forward(20)


screen = turtle.Screen()
screen.title("Random Walk ^_^")
screen.screensize(1000, 1000)
screen.exitonclick()