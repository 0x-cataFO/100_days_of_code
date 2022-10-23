from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
length = len(question_data)
for number in range(length):
    text = question_data[number]["text"]
    answer = question_data[number]["answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
