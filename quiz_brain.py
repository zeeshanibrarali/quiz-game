
# TODO: asking the question
class Quiz:
    def __init__(self, list_of_question):
        self.question = 0
        self.questions = list_of_question
        self.score = 0

    def still_has_questions(self):
        return self.question < len(self.questions)

    def next_question(self):
        current_question = self.questions[self.question]
        self.question += 1
        ans = input(f'Q.{self.question}: {current_question.text} (true/false)? ').title()
        self.check_answer(ans, current_question.answer)

    def check_answer(self, user, pc):
        if user == pc:
            print('You\'re right')
            self.score += 1
        else:
            print('You\'re wrong')
        print(f'The right answer is {pc}')
        print(f'Your current score is : {self.score}/{self.question} ')
        print('\n')
