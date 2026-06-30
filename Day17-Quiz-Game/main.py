from question_model import Question
from quiz_brain import QuizBrain
import data


question_bank = []
for qstn_dict in data.question_data:
    question_text = qstn_dict['text']
    question_answer = qstn_dict['answer']

    new_question = Question(q_text=question_text, q_ans=question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(q_list=question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score: {quiz_brain.score}/{quiz_brain.question_number}")
