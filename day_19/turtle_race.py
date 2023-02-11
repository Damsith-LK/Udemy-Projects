import turtle
from random import randint

screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)
screen.bgcolor('black')
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win. Enter a color: ").lower()
colors = ['red', 'green', 'yellow', 'purple', 'orange', 'blue']

if bet not in colors:
    screen.clear()
    quit()

red = turtle.Turtle(shape='turtle')
green = turtle.Turtle(shape='turtle')
yellow = turtle.Turtle(shape='turtle')
purple = turtle.Turtle(shape='turtle')
orange = turtle.Turtle(shape='turtle')
blue = turtle.Turtle(shape='turtle')

red.color('red')
green.color('green')
yellow.color('yellow')
purple.color('purple')
orange.color('orange')
blue.color('blue')

red.penup()
green.penup()
yellow.penup()
purple.penup()
orange.penup()
blue.penup()

red.goto(x=-230, y=150)
green.goto(x=-230, y=100)
yellow.goto(x=-230, y=50)
purple.goto(x=-230, y=0)
orange.goto(x=-230, y=-50)
blue.goto(x=-230, y=-100)


def main():
    first = None
    while True:
        red.forward(randint(1, 5))
        green.forward(randint(1, 5))
        yellow.forward(randint(1, 5))
        purple.forward(randint(1, 5))
        orange.forward(randint(1, 5))
        blue.forward(randint(1, 5))
        red_pos = red.xcor()
        green_pos = green.xcor()
        yellow_pos = yellow.xcor()
        purple_pos = purple.xcor()
        orange_pos = orange.xcor()
        blue_pos = blue.xcor()
        if red_pos >= 250:
            first = 'red'
            break
        elif green_pos >= 250:
            first = 'green'
            break
        elif yellow_pos >= 250:
            first = 'yellow'
            break
        elif purple_pos >= 250:
            first = 'purple'
            break
        elif orange_pos >= 250:
            first = 'orange'
            break
        elif blue_pos >= 250:
            first = 'blue'
            break

    if bet == first:
        print(f'Your bet was right. The first was {first}')
    else:
        print(f'Your bet was wrong. The first was {first}')


main()
screen.exitonclick()