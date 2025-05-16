from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    ques = Question(q["text"], q["answer"])
    question_bank.append(ques)


q = QuizBrain(question_bank)
while q.still_has_question():
    q.next_question()


print(f"You have completed the quiz\nYour final score is: {q.score}/{q.question_number}")