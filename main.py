from data import question_data
from quiz_brain import QuizBrain
from question_model import Question
question_bank=[]
for i in range(0,len(question_data)):
    question=Question(question_data[i]['question'],question_data[i]['correct_answer'])
    question_bank.append(question)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You Have completed the Quiz")
print(f"Your Final Score Was: {quiz.score}/{quiz.question_number}")