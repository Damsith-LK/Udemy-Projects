from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    obj = Question(i['question'], i['correct_answer'])
    question_bank.append(obj)

quiz = QuizBrain(question_bank)

while True:
    quiz.next_question()
    if not quiz.still_has_question():
        break

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.list)}")