from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_cnt = 0
valid = False
while not valid:
    try:
        question_cnt = int(input("How many questions do you want to try? "))
        valid = True
    except:
        print("Invalid input")

question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank, question_cnt)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_total}")
