# Here we are going to make a workout tracker program with nutritionix API and also using google sheets
# 2023/05/16 - Making a UI for this

from tkinter import *
import config
import requests
import datetime

GENDER = "male"
END_POINT = "https://trackapi.nutritionix.com"

# ----------------------- SUBMIT FUNCTION ------------------------- #

def submit():

    # Checking for faults in day entry
    day = selected_date.get().lower()
    if day == 'day before yesterday':
        day = datetime.datetime.now() - datetime.timedelta(days=2)
    elif day == "yesterday":
        day = datetime.datetime.now() - datetime.timedelta(days=1)
    else:
        day = datetime.datetime.now()
    day = day.strftime("%d/%m/%Y")

    # Checking for faults in time entry
    time_ = time_entry.get().lower()
    if ":" not in time_ and time_ != "now":
        quit("Invalid Input")
    if time_ == "now":
        time_ = datetime.datetime.now().strftime("%X")
    else:
        time_ += ":00"

    exercises = exercises_entry.get()

    # Getting relevant information about the workout from nutritionix API
    exercise_params = {
        "query": exercises,
        "gender": GENDER,
        "weight_kg": 38,
        "height_cm": 163.5,
        "age": 15
    }
    exercise_headers = {
        "x-app-id": config.NIX_ID,
        "x-app-key": config.NIX_KEY,
    }

    exercise_response = requests.post(url=f"{END_POINT}/v2/natural/exercise", json=exercise_params,
                                      headers=exercise_headers)
    data = exercise_response.json()
    print(data)

    # Sending the information to the Google Sheet via Sheety API
    sheet_header = {"Authorization": config.SHEETY_TOKEN}

    for exercise in data["exercises"]:
        sheet_inputs = {
            "workout": {
                "date": day,
                "time": time_,
                "exercise": exercise["name"].title(),
                "duration": "{} mins".format(str(exercise["duration_min"])),
                "calories": exercise["nf_calories"]
            }
        }

        sheet_response = requests.post(config.SHEETY_ENDPOINT, json=sheet_inputs, headers=sheet_header)

        print(sheet_response.text)

    # Destroying the window after submitting
    root.destroy()

# ----------------------------- SUBMIT FUNCTION END HERE --------------------------- #

# Constants
WINDOW_COLOR = "#3C486B"
BORDER_COLOR = "#F0F0F0"
TEXT_COLOR = "#F9D949"
TOPIC_COLOR = "#F45050"
HIGHLIGHT_COLOR = "#F0FF42"
TEXT_FONT = ("Ariel", 11, "bold")

# --------------------------------- UI Setup ------------------------------------------ #
# Creating the window
root = Tk()
root.config(bg=WINDOW_COLOR, pady=20, padx=20)
root.title("Workout Tracker")

# Topic
topic_label = Label(text="Workout Tracker made using Python", fg=TOPIC_COLOR, font=("Times New Roman", 23, "underline"), bg=WINDOW_COLOR, pady=20)
topic_label.grid(column=1, row=0)

exercises_label = Label(text="Exercises you did: ", bg=WINDOW_COLOR, fg=TEXT_COLOR, font=TEXT_FONT)
exercises_label.grid(column=0, row=1, sticky="e")

exercises_entry = Entry(border=2, width=105, fg="black", highlightcolor=HIGHLIGHT_COLOR, highlightthickness=3)
exercises_entry.grid(column=1, row=1, columnspan=2, pady=10)

time_label = Label(text="Time (example input - 18:30): ", bg=WINDOW_COLOR, fg=TEXT_COLOR, font=TEXT_FONT)
time_label.grid(column=0, row=2, pady=10, sticky="e")

time_entry = Entry(border=2, width=105, fg="black", highlightcolor=HIGHLIGHT_COLOR, highlightthickness=3)
time_entry.insert(0, "now")
time_entry.grid(column=1, row=2, columnspan=2, pady=10)

# Date label and an Option Menu for choosing the date
date_label = Label(text="Date: ", bg=WINDOW_COLOR, fg=TEXT_COLOR, font=TEXT_FONT)
date_label.grid(column=0, row=3, sticky="e")
selected_date = StringVar()
dates = ["Today", "Yesterday", "Day Before Yesterday"]
selected_date.set(dates[0])
drop_box = OptionMenu(root, selected_date, *dates)
drop_box.config(fg="blue", bg=HIGHLIGHT_COLOR, font=TEXT_FONT, activebackground=TOPIC_COLOR)
drop_box.grid(column=1, row=3, sticky="w", pady=10)

# The submit button - using lambda function in order to input multiple commands at once
submit_button = Button(text="Submit", font=TEXT_FONT, bg="#F97B22", activebackground="cyan", command=submit)
submit_button.grid(column=2, row=4)

root.mainloop()