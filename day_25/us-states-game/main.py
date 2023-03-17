"""
Steps for this States game

1. Set up the screen and the background - Done
2. Get the input from the user (and turn it into title case) - Done
3. Check if the answer is among 50_states.csv - Done
4. Write correct answers into map
5. Use a loop to allow the user to keep answering
6. Record the correct answers in a list
7. Keep track of the score
"""


import turtle
import pandas as pd

turtle.tracer(0)
# Setting the screen
screen = turtle.Screen()
screen.setup(width=720, height=510)
screen.title("U.S. States Game")

# Setting up the background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Getting the data
data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
x = data["x"].to_list()
y = data["y"].to_list()

game_continue = True

# Game loop
correct_states = []

while game_continue:
    answer = screen.textinput(title="Answer the states", prompt="Enter a state name ").title()
    print(answer)

    # Checking the rightness
    if answer in states:
        ind = states.index(answer)


    else:
        print("bad")


screen.exitonclick()