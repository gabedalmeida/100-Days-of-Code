from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
    

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_a_question:
    quiz.next_question()
    
print("You\'ve complete the quiz!")
print(f"You score was {quiz.score} / {quiz.question_number}")