from tkinter import *

# Got these colors from colorhunt.io
BG = "#FF6D60"
LABEL_COLOR = "#F7D060"
BORDER_COLOR = "#F3E99F"
IMAGE_BORDER_COLOR = "#98D8AA"
BUTTON_PRESS_COLOR = "cyan"


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Habit Tracker")
        self.window.config(bg=BG, padx=50, pady=50)
        self.window.update_idletasks()  # update the window size info
        self.window.minsize(self.window.winfo_width(), self.window.winfo_height())

        image = PhotoImage(file="meditation.png")
        self.canvas = Canvas(width=450, height=475)
        self.image = self.canvas.create_image(225, 234, image=image)
        self.canvas.config(highlightbackground=IMAGE_BORDER_COLOR, highlightthickness=10)
        self.canvas.grid(column=0, row=0)

        self.day_label = Label(text="Which day you want to update: ")
        self.day_label.config(font=("sans-serif", 16, "bold"), bg=BG, fg=LABEL_COLOR)
        self.day_label.grid(column=0, row=1, sticky="e")

        self.day_entry = Entry(width=50)
        self.day_entry.config(highlightcolor=BORDER_COLOR, highlightthickness=3)
        self.day_entry.focus()
        self.day_entry.insert(0, "Yesterday")
        self.day_entry.grid(column=1, row=1, columnspan=2)

        self.minutes_label = Label(text="Number of minutes you meditated (An int or a float is expected): ")
        self.minutes_label.config(font=("sans-serif", 16, "bold"), bg=BG, fg=LABEL_COLOR)
        self.minutes_label.grid(column=0, row=2)

        self.minutes_entry = Entry(width=50)
        self.minutes_entry.config(highlightcolor=BORDER_COLOR, highlightthickness=3)
        self.minutes_entry.grid(column=1, row=2, columnspan=2)

        self.button = Button(text="Submit")
        self.button.config(relief="raised", width=45, activebackground=BUTTON_PRESS_COLOR)
        self.button.grid(column=1, row=3)

        self.window.mainloop()

gui = GUI()