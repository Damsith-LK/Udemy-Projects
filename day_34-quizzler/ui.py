from tkinter import *
from quiz_brain import QuizBrain
from tkinter.ttk import Combobox

THEME_COLOR = "#375362"

cat_list = [
    "General Knowledge", "Books", "Film", "Music", "Musicals & Theatres", "Television", "Video Games", "Board Games",
    "Nature", "Computers", "Mathematics", "Mythology", "Sports", "Geography", "History", "Politics", "Art", "Celebrities",
    "Animals", "Vehicles", "Comics", "Gadgets", "Japanese Anime and Manga",
    "Cartoon & Animations"
            ]

categories = {key: cat_list.index(key) + 9 for key in cat_list}


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Times New Roman", 15, 'bold'))
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

        self.combo = Combobox(values=cat_list)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>")
        self.combo.grid(column=0, row=0)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(command=self.window.destroy)

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

    def select_category(self):
        cat = self.combo.get()
        if cat in cat_list:
            return categories[cat]
        else:
            self.window.destroy()
