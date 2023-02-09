import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('arrow')

# Drawing a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

screen = turtle.Screen()
screen.exitonclick()