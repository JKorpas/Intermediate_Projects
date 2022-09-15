from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = [Question(question["category"], question["question"], question["correct_answer"])
                 for question in question_data]


quiz = QuizBrain(question_bank)
#pass quiz brain type to ui 
quiz_interface = QuizInterface(quiz)






