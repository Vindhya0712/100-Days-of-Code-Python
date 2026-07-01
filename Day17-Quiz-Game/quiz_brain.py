class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.correct_answers = 0
        self.wrong_answers = 0


    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            return False
        else:
            return True


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ask_user = input(f"Q{self.question_number} of {len(self.question_list)}\n{'-' * 100} \n{current_question.text} "
                         f"(True/False): ").lower()

        while ask_user not in ['true', 'false']:
            print("Invalid Input. Please try entering True or False.")
            ask_user = input(f"Q{self.question_number}: {current_question.text} (True/False): ").strip().lower()
            if ask_user == 'True' or ask_user == 'False':
                break

        self.check_answer(ask_user, current_question.answer)



    def check_answer(self, u_ans, c_ans):
        if u_ans == c_ans.lower():
            self.score += 1
            self.correct_answers += 1
            print(f"Yay, you got it!")

        else:
            self.wrong_answers += 1
            print(f"Sorry, that was wrong.")
            print(f"The correct answer was: {c_ans}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")



