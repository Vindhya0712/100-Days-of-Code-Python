class Question:
    def __init__(self, q_text, q_ans):
        self.text = q_text
        self.answer = q_ans


new_question = Question("The question's text", "The answer's text")
print(new_question.text)
