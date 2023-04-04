from tkinter import *

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 10, 'bold'))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.canvas.create_text(150, 125, font=("Ariel", 15, 'italic'), text="Amazon acquired Twitch in\n"
                                                        "August 2014 for 970 million\n"
                                                        "dollars."
                                                        )

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, bg=THEME_COLOR)
        self.false_button = Button(image=self.false_img, bg=THEME_COLOR)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()