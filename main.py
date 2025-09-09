from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_score = QuizBrain(0)
while QuizBrain.still_has_questions:
    # loop through list of questions except index error for dynamic list length.
    try:
        quiz.next_question()
    except IndexError:
        QuizBrain.still_has_questions = False

print(f"Game Over!\n Final Score: {quiz.correct} correct, {quiz.wrong} wrong.")
