import turtle

my_turtle = turtle.Turtle()

# Drawing a dashed line
for _ in range(5):
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

screen = turtle.Screen()
screen.exitonclick()