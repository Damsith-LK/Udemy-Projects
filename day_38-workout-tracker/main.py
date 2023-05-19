# Here we are going to make a workout tracker program with nutritionnix API and also using google sheets
# 2023/05/16 - Making a UI for this

from tkinter import *
import config
import requests
import datetime

# Constants
WINDOW_COLOR = "#3C486B"
BORDER_COLOR = "#F0F0F0"
TEXT_COLOR = "#F9D949"
TOPIC_COLOR = "#F45050"
HIGHLIGHT_COLOR = "#F0FF42"
TEXT_FONT = ("Ariel", 11, "bold")
GENDER = "male"
END_POINT = "https://trackapi.nutritionix.com"

exercise_params = {
    "query": input("What exercises did you do: "),
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


# ----------------------- FUNCTIONS START HERE ------------------------- #
def get_date() -> str:
    day = input("When did you do these exercises? (day before yesterday or yesterday or today): ").lower()
    if day == 'day before yesterday':
        day = datetime.datetime.now() - datetime.timedelta(days=2)
    elif day == "yesterday":
        day = datetime.datetime.now() - datetime.timedelta(days=1)
    else:
        day = datetime.datetime.now()

    return str(day.strftime("%d/%m/%Y"))

def get_time() -> str:
    time = input("At what time of the day did you these glorious exercises (eg - 18:30 or now): ").lower()
    if ":" not in time and time != "now":
        quit("Invalid Input")
    if time == "now":
        time = datetime.datetime.now().strftime("%X")
    else:
        time += ":00"

    return time
# ----------------------------- FUNCTIONS END HERE --------------------------- #


date = get_date()
time = get_time()
print(date, time)

sheet_header = {"Authorization": config.SHEETY_TOKEN}

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": "{} mins".format(str(exercise["duration_min"])),
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(config.SHEETY_ENDPOINT, json=sheet_inputs, headers=sheet_header)

    print(sheet_response.text)


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

# The submit button
submit_button = Button(text="Submit", font=TEXT_FONT, bg="#F97B22", activebackground="cyan")
submit_button.grid(column=2, row=4)

root.mainloop()