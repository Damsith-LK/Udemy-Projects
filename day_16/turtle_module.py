import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.shapesize(5, 5, 12)
my_turtle.color('red', 'green')

# Getting the turtle to move forward by 100 paces
my_turtle.forward(100)

my_screen = turtle.Screen()  
my_screen.exitonclick()

# You can learn about this package if needed, from the official documentation