import turtle
from random import randint

my_turtle = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()
screen.title("Spirograph")


# Generating random rgb colors:
def rand_rgb():
    colors = (randint(0, 255), randint(0, 255), randint(0, 255))
    return colors


# Drawing the spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.pencolor(rand_rgb())
        my_turtle.speed('fastest')
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)


draw_spirograph(3)
screen.exitonclick()