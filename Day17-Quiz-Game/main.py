from question_model import Question
from quiz_brain import QuizBrain
import data
import prettytable
import random


def quiz_game():
    question_bank = []
    for qstn_dict in data.question_data:
        question_text = qstn_dict['question']
        question_answer = qstn_dict['correct_answer']

        new_question = Question(q_text=question_text, q_ans=question_answer)
        question_bank.append(new_question)
    random.shuffle(question_bank)

    quiz_brain = QuizBrain(q_list=question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.next_question()


    score = quiz_brain.score
    accuracy = round((score/len(question_bank)) * 100, 2)

    if accuracy == 100:
        print("Outstanding! Perfect score! 🎉\nBelow are your complete stats: ")
    elif 80 <= accuracy <= 99:
        print("Excellent! 👏\nBelow are your complete stats: ")
    elif 60 <= accuracy <= 79:
        print("Good job! 👍\nBelow are your complete stats: ")
    else:
        print("Nice work! Keep Practicing! 😄\nBelow are your complete stats: ")


    table = prettytable.PrettyTable()

    table.field_names = ['Info', 'Stats']
    table.add_row(['Score', f"{quiz_brain.score}/{quiz_brain.question_number}"])
    table.add_row(['Correct Answers', f"{quiz_brain.correct_answers}"])
    table.add_row(['Wrong Answers', f"{quiz_brain.wrong_answers}"])
    table.add_row(['Accuracy', f"{accuracy:.2f}%"])
    table.align = 'l'
    print(table)


quiz_game()
continue_playing = True
while continue_playing:
    play_again = input("""\nDo you want to play again?
1. Yes
2. No
Enter your choice: """)
    if play_again.isdigit():
        play_again = int(play_again)
        if play_again == 1:
            print('\n')
            quiz_game()
        elif play_again == 2:
            print("Goodbye! Game Exiting ...")
            continue_playing = False
        else:
            print("Invalid Choice. Try choosing one of the options from the menu.")
    else:
        print("Invalid Choice. Try choosing one of the options from the menu.")