from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_bank = []
for q in question_data:
    question = Question(q['question'], q['correct_answer'])
    question_bank.append(question)

quiz = Quiz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print('You have completed the Quiz')
print(f'You have scored {quiz.score}/{quiz.question}')
