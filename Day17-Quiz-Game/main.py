import random, data

already_asked = []


def choose_question():
    qstn = random.choice(data.question_data)

    while qstn in already_asked:
        qstn = random.choice(data.question_data)

    already_asked.append(qstn)

    if already_asked == data.question_data:
        return None
    else:
        return qstn


def display_question_ask_answer(qstn, cnter):
    print(f"\nQuestion {cnter + 1}/12 \n{qstn['text']}")
    answer = input("Is the above statement True or False? ").title()
    cnter += 1
    return answer


def check_answer(u_ans, qst):
    if u_ans == qst['answer']:
        print("Yes, you got it!")
        return True
    else:
        print("Sorry, that wasn't the correct answer.")
        return False


def initialize_player():
    p_name = input("Enter player name: ").title()
    p_score = 0
    return p_name, p_score


def game():
    player_name, player_score = initialize_player()
    print(f"Welcome to Quiz Brain, {player_name}\nYour current score: {player_score}")

    counter = 0
    continue_choosing = True
    while continue_choosing:
        question = choose_question()
        if question is not None:
            answer = display_question_ask_answer(question, counter)
            if check_answer(u_ans=answer, qst=question):
                player_score += 1
                print(f"Your current score: {player_score}")
            else:
                print(f"Your current score: {player_score}")
        else:
            print("\nRan out of questions. Have to abort. \nThank you for playing.")


game()
