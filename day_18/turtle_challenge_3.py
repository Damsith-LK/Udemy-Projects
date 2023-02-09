import turtle
from random import choice

my_turtle = turtle.Turtle()

degrees = [120, 90, 72, 60, 360/7, 45, 40, 36]
colors = ['red', 'green', 'black', 'blue', 'pink', 'navy', 'orange', 'gold']


# Defining the function
def draw_shape(color, pos_in_degrees_list):
    turtle.pencolor(color)
    for i in range(pos_in_degrees_list + 3):
        turtle.forward(150)
        turtle.right(degrees[pos_in_degrees_list])


# Drawing bunch of shapes on each other with randomized colors
for i in range(0, len(degrees)):
    rand_color = choice(colors)
    colors.remove(rand_color)
    draw_shape(rand_color, i)


screen = turtle.Screen()
screen.exitonclick()