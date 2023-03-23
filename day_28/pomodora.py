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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(300)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(secs):
    minutes = floor(secs / 60)
    seconds = secs % 60

    if seconds == 0:
        canvas.itemconfig(timer_text, text=f"{minutes}:00")
    else:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if secs > 0:
        window.after(1000, count_down, secs - 1)

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
