import random, art


def validate_integer(variable):
    if variable.isdigit():
        return int(variable)
    else:
        return None


def no_of_attempts(level):
    if level == 1:
        chances = 10
        return chances
    elif level == 2:
        chances = 5
        return chances
    else:
        return None


def print_attempts_left(chances):
    print(f"You have {chances} remaining to guess the number.")


def game():
    def boot_game():
        print(art.logo)
        print("""Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100. """)

        continue_ask = True

        while continue_ask:

            difficulty = input("Choose a difficulty level:\n1. Easy\n2. Hard\nType the number against your choice: ")
            difficulty_level = validate_integer(difficulty)

            if difficulty_level == 1 or difficulty_level == 2:
                attempts = no_of_attempts(difficulty_level)
                print(f"\nYou have {attempts} remaining to guess the number.\n")
                continue_ask = False
                status = game_logic(difficulty_level)
                if status == "Game Over.":
                    return
            else:
                print("\nInvalid Input. \nPlease choose either 1 or 2 from the menu.\n")
                continue_ask = True

    def game_logic(game_level):
        chosen_number = random.randint(1, 100)
        continue_game = True
        attempts = no_of_attempts(game_level)
        while continue_game:
            user_guess = input("Make a guess: ")
            guess = validate_integer(user_guess)

            if guess is not None:
                if guess > chosen_number:
                    print("Too high. ⬆️")
                    attempts -= 1
                    if attempts > 0:
                        print_attempts_left(attempts)
                    if attempts == 0:
                        print(f"You've run out of guesses. {chosen_number} was the answer. 😭")
                        return "Game Over."
                elif guess < chosen_number:
                    print("Too low. ⬇️")
                    attempts -= 1
                    if attempts > 0:
                        print_attempts_left(attempts)
                    if attempts == 0:
                        print(f"You've run out of guesses. {chosen_number} was the answer. 😭")
                        return "Game Over."
                else:
                    print(f"You got it! The answer was {chosen_number} 😎")
                    return "Game Over."
            else:
                print("\nInvalid Guess. \nPlease try guessing an integral value between 0 and 100.\n")

    boot_game()


game()
