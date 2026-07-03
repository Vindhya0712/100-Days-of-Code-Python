from question_model import Question
from quiz_brain import QuizBrain
import data
import prettytable
import random


def quiz_game_logic():
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
    accu = round((score/len(question_bank)) * 100, 2)

    if accu == 100:
        print("Outstanding! Perfect score! 🎉\nBelow are your complete stats: ")
    elif 80 <= accu <= 99:
        print("Excellent! 👏\nBelow are your complete stats: ")
    elif 60 <= accu <= 79:
        print("Good job! 👍\nBelow are your complete stats: ")
    else:
        print("Nice work! Keep Practicing! 😄\nBelow are your complete stats: ")


    table = prettytable.PrettyTable()

    table.field_names = ['Info', 'Stats']
    table.add_row(['Score', f"{quiz_brain.score}/{quiz_brain.question_number}"])
    table.add_row(['Correct Answers', f"{quiz_brain.correct_answers}"])
    table.add_row(['Wrong Answers', f"{quiz_brain.wrong_answers}"])
    table.add_row(['Accuracy', f"{accu:.2f}%"])
    table.align = 'l'
    print(table)



def play_quiz():
    continue_game = True
    while continue_game:
        gamer_name = input("Enter player name: ").lower()
        print(f"\nWelcome to the Quiz Game, {gamer_name}")
        quiz_game_logic()
        continue_with_same_user = True
        while continue_with_same_user:
            play_again = input("""\nDo you want to play again?
1. Yes! I wanna go again
2. No, but let's switch to a different user
3. No, and exit the game
Enter your choice: """)
            if play_again.isdigit():
                play_again = int(play_again)
                if play_again == 1:
                    print('\n')
                    quiz_game_logic()

                elif play_again == 2:
                    print(f"Goodbye {gamer_name}! \nHope to see you again.\n")
                    continue_with_same_user = False

                elif play_again == 3:
                    print("Goodbye! Game Exiting...")
                    continue_with_same_user = False
                    continue_game = False

                else:
                    print("Invalid Choice. Try choosing one of the options from the menu.")
            else:
                print("Invalid Choice. Try choosing one of the options from the menu.")


play_quiz()
