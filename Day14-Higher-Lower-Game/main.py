import random, game_data, art, os


#TODO - 1: Pick 2 random people -- Person A and Person B
    #TODO 1.1 - The game data is in a list of dictionaries
    #TODO 1.2 - How do you find two random values from there?
    #Remember that a list of dictionaries is still a list -- use the random.choice() method
#TODO - 2: Ask the user to guess who has more Instagram followers
#TODO - 3: Validate the user's guess
#TODO - 4: If the user guessed correctly
    #TODO - 4.1: Person B becomes new Person A
    #TODO - 4.2: Find a new Person B
    #TODO - 4.3: Continue the game
#TODO - 5: If the user fails to guess correctly
    #TODO - 5.1: Exit the game
    #TODO - 5.2: On a clear screen, print his score


def higher_lower_game():
    person_a = random.choice(game_data.data)
    score = 0
    def choose_people(person1):
        person2 = random.choice(game_data.data)
        while person1 == person2:
            person2 = random.choice(game_data.data)

        return person2

    person_b = choose_people(person_a)

    def check_repetition(p1, p2):
        while p1 == p2:
            p2 = random.choice(game_data.data)
        return p1, p2

    def find_answer(p1, p2):
        if p1['follower_count'] > p2['follower_count']:
            return p1['name']
        elif p1['follower_count'] < p2['follower_count']:
            return p2['name']
        else:
            return random.choice([p1['name'], p2['name']])

    def validate_guess(user_guess, current_score, person1, person2):
        if user_guess == 'A':
            g_name = person1['name']
            answer_name = find_answer(person1, person2)
            if g_name == answer_name:
                current_score += 1
                print(f"You're right. Current score: {current_score}")
                person1 = person2
                person2 = choose_people(person1)
                person1, person2 = check_repetition(person1, person2)
                return True, current_score, person1, person2
            else:
                return False, current_score, person1, person2

        elif user_guess == 'B':
            g_name = person2['name']
            answer_name = find_answer(person1, person2)
            if g_name == answer_name:
                current_score += 1
                print(f"You're right. Current score: {current_score}")
                person1 = person2
                person2 = choose_people(person1)
                person1, person2 = check_repetition(person1, person2)
                return True, current_score, person1, person2
            else:
                return False, current_score, person1, person2

    os.system("cls")
    continue_game = True
    while continue_game:
        os.system("cls")
        guess = input(f"""{art.logo}
Compare A: {person_a['name']}, {person_a['description']} from {person_a['country']}
{art.vs}
Against B: {person_b['name']}, {person_b['description']} from {person_b['country']}
Who do you think has more followers? Type 'A' or 'B': """).strip().upper()

        if guess != 'A' and guess != 'B':
            print("Invalid Input. Please try choosing A or B.")
            os.system("cls")
        else:
            continue_game, score, person_a, person_b = validate_guess(guess, score, person_a, person_b)
            if continue_game is False:
                os.system("cls")
                print(f"""{art.logo}\nSorry, that was wrong. Final score: {score}""")
                break

higher_lower_game()
continue_playing = True
while continue_playing:
    play_again = input("Do you want to play again? \n1. Yes\n2. No\nType your choice: ")
    if play_again.isdigit():
        play_again = int(play_again)
        if play_again == 1:
            higher_lower_game()
            continue_playing = True
        elif play_again == 2:
            continue_playing = False
            print("Goodbye! Game exiting.")
        else:
            print("Invalid Input. Please try choosing 1 or 2.")
    else:
        print("Invalid Input. Please try choosing 1 or 2.")