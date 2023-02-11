# How the key pressing works:
# 1. W = Forwards
# 2. S = Backwards
# 3. A = Left
# 4. D = Right
# 5. C = Clear and get the turtle to the original position

import turtle

screen = turtle.Screen()
screen.title("Etch-a-Sketch game")
t = turtle.Turtle()


def forward():
    t.forward(20)


def backward():
    t.backward(20)


def left():
    t.left(20)


def right():
    t.right(20)


def clear():
    t.reset()
    t.showturtle()


screen.onkey(fun=forward, key='w')
screen.onkey(fun=backward, key='s')
screen.onkey(fun=right, key='d')
screen.onkey(fun=left, key='a')
screen.onkey(fun=clear, key='c')
screen.listen()

screen.exitonclick()

