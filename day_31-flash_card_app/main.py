from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("french_words.csv")
words = data.to_dict(orient="records")
rand_word = {}

# -------------- User knows the word or not ----------------------------------------------- #

def knows():
    word_display()
    words.remove(rand_word)

def not_knows():
    word_display()
    try:
        to_learn_data = pd.read_csv("words_to_learn.csv")
    except FileNotFoundError:
        data.to_csv("words_to_learn.csv", index=False)
    else:
        to_learn_data.append(rand_word)

# ----------------------------- Flip the cards ------------------------------------------- #

def flip_cards(english_word):
    canvas.itemconfig(win_img, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")

# ---------------------- Reading the csv file and associating with the GUI --------------------------- #

def word_display():
    global flip_timer
    global rand_word
    window.after_cancel(flip_timer)
    rand_word = choice(words)
    canvas.itemconfig(win_img, image=front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=rand_word["French"], fill="Black")

    flip_timer = window.after(3000, flip_cards, rand_word["English"])


# -------------------------- UI Setup ------------------------------ #
window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_cards)

back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
win_img = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=word_display)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

word_display()

window.mainloop()