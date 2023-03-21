"""
Steps for this States game

1. Set up the screen and the background - Done
2. Get the input from the user (and turn it into title case) - Done
3. Check if the answer is among 50_states.csv - Done
4. Write correct answers into map - Done
5. Use a loop to allow the user to keep answering - Done
6. Record the correct answers in a list - Done
7. Keep track of the score - Done
8. Game over when all the states are been named - Done

Additional objective - when prompted "Exit", close the game and save the not answered states to a file called states_to_learn.csv
"""


import turtle
import pandas as pd
from time import sleep

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

t = turtle.Turtle(visible=False)
t.penup()

# Game loop
correct_states = []

while len(correct_states) < 50:
    answer = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="Enter a state name ").title()

    # The additional objective here
    if answer == "Exit":
        missing_states = [i for i in states if i not in correct_states]
        data_frame = pd.DataFrame(missing_states)
        data_frame.to_csv("states_to_learn.csv")
        quit()

    # Checking the rightness
    if answer in states:
        ind = states.index(answer)
        t.goto(x[ind], y[ind])
        t.write(arg=answer, move=False, align='center', font=("Ariel", 7, "bold"))

        if answer not in correct_states:
            correct_states.append(answer)

t.goto(0, 0)
t.write(arg="GAME OVER. YOU WON", move=False, align="center", font=("Ariel", 15, "bold"))
sleep(4)