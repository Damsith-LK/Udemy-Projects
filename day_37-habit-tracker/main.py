# In this program, we'll be using not only get() but also post()
# I'm using this to keep track of my meditation

from tkinter import *
import requests
import config
import datetime
from datetime import timezone

# Got these colors from colorhunt.io
BG = "#FF6D60"
LABEL_COLOR = "#F7D060"
BORDER_COLOR = "#F3E99F"
IMAGE_BORDER_COLOR = "#98D8AA"
BUTTON_PRESS_COLOR = "cyan"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# # creating the user
user_params = {
    "token": config.TOKEN,
    "username": config.USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# # created the user

# Creating a graph
graph_params = {
    "id": "graph1",
    "name": "Meditation",
    "unit": "minutes",
    "type": "float",
    "color": "momiji"  # momoji == red
}
headers = {"X-USER-TOKEN": config.TOKEN}
# graph_response = requests.post(url=f"{PIXELA_ENDPOINT}/{config.USERNAME}/graphs", json=graph_params, headers=headers)
# print(graph_response.text)
# created the graph

def check_minutes(minutes: float) -> float:
    """Checks the given minutes and returns it if it is valid. Else returns 0"""
    if minutes == 0:
        return 0
    elif minutes < 0:
        return abs(minutes)
    else:
        return minutes

def submit():
    """Gets the data from the entry fields and updates them into the graph"""
    day = day_entry.get().lower()
    minutes = minutes_entry.get()

    if day == 'day before yesterday':
        date = datetime.datetime.now() - datetime.timedelta(days=2)
    elif day == "yesterday":
        date = datetime.datetime.now() - datetime.timedelta(days=1)
    else:
        date = datetime.datetime.now()

    # Updating the graph
    update_params = {
        "date": str(date.strftime("%Y%m%d")),
        "quantity": str(check_minutes(float(minutes)))
    }
    update_response = requests.post(url=f"{PIXELA_ENDPOINT}/{config.USERNAME}/graphs/graph1", json=update_params, headers=headers)
    print(update_response.text)

    # Window will stay alive if the API post is rejected, so user can try again
    if update_response.json()["isSuccess"]:
        window.destroy()



# -------------------------- UI Setup ------------------------------- #
window = Tk()
window.title("Habit Tracker")
window.config(bg=BG, padx=50, pady=50)
window.update_idletasks()  # update the window size info
window.minsize(window.winfo_width(), window.winfo_height())

day_label = Label(text="Which day you want to update: ")
day_label.config(font=("sans-serif", 16, "bold"), bg=BG, fg=LABEL_COLOR)
day_label.grid(column=0, row=1, sticky="e")

day_entry = Entry(width=50)
day_entry.config(highlightcolor=BORDER_COLOR, highlightthickness=3)
day_entry.focus()
day_entry.insert(0, "Yesterday")
day_entry.grid(column=1, row=1, columnspan=2)

minutes_label = Label(text="Number of minutes you meditated (An int or a float is expected): ")
minutes_label.config(font=("sans-serif", 16, "bold"), bg=BG, fg=LABEL_COLOR)
minutes_label.grid(column=0, row=2)

minutes_entry = Entry(width=50)
minutes_entry.config(highlightcolor=BORDER_COLOR, highlightthickness=3)
minutes_entry.grid(column=1, row=2, columnspan=2)

button = Button(text="Submit")
button.config(relief="raised", width=45, activebackground=BUTTON_PRESS_COLOR, command=submit)
button.grid(column=1, row=3)

window.mainloop()