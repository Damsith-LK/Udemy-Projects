from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Timer New Roman", 15, 'bold'))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.q_text = self.canvas.create_text(150, 125, font=("Ariel", 15, 'italic'),
                                              text="The Question here",
                                              width=290)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, bg=THEME_COLOR, command=self.true)
        self.false_button = Button(image=self.false_img, bg=THEME_COLOR, command=self.false)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=q_text)

    def true(self):
        self.quiz.check_answer("True")

    def false(self):
        self.quiz.check_answer("False")
