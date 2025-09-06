class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct = 0
        self.wrong = 0

    def still_has_questions(self):
        more_questions = True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = current_question.answer.lower()
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        if user_answer == "true" or user_answer == "false":
            if answer == user_answer:
                self.correct += 1
            else:
                self.wrong += 1

        else:
            return input("Incorrect input, please try again (True/False): ").lower()

        self.show_score()

    def show_score(self):
        print(f"Current score: {self.correct} correct and {self.wrong} wrong.")
