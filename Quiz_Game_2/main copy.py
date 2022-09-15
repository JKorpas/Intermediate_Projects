from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

'''
for index, question in enumerate(question_data):
    index = Question(question["text"], question["answer"])
    question_bank.append(index)'''

question_bank = [Question(question["category"], question["question"], question["correct_answer"])
                 for question in question_data]
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
