from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0  # This is not a constant
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_sec)
        label.config(text="Break")
    elif reps % 2 == 1:
        count_down(work_sec)
        label.config(text="Work")
    else:
        count_down(short_sec)
        label.config(text="Break")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(secs):
    minutes = floor(secs / 60)
    seconds = secs % 60

    if seconds < 10:
        canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if secs > 0:
        window.after(1000, count_down, secs - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating the canvas and adding the picture here:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"), highlightthickness=0)
label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=3)

ticks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, 'bold'))
ticks.grid(row=3, column=1)

window.mainloop()
