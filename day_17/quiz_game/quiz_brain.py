class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.list = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(answer, current_question.answer)

    def still_has_question(self):
        if self.list[self.question_number] == self.list[-1]:
            return False
        else:
            self.question_number += 1
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n\n")
