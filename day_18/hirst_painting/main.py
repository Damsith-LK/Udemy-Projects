# The size of a dot must be 20 and 50 of space between each other
# Total of 100 dots


from getting_rgb import color_codes as colors
import turtle
from random import choice

turtle.colormode(255)
screen = turtle.Screen()
screen.title("Hirst painting - My Version")

my_turtle = turtle.Turtle()
my_turtle.penup()

# Doing the hirst art
my_turtle.setpos(-200, -200)

for i in range(10):
    my_turtle.speed('fastest')
    my_turtle.setpos(-200, -200 + i * 50)
    for _ in range(10):
        my_turtle.speed('slow')
        color = choice(colors)
        my_turtle.dot(20, color)
        my_turtle.forward(50)

my_turtle.hideturtle()


screen.exitonclick()