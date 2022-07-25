from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for dictionary in question_data:
    question_bank.append(Question(dictionary["question"],dictionary["correct_answer"]))

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print(f"You've completed the quiz!")
print(f"Your final score is: {quiz_brain.current_score}")



# while quiz_brain.question_number !=len(question_bank):
#    quiz_brain.next_question()

