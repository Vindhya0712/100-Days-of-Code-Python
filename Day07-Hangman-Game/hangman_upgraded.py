import random, hangman_art, hangman_words


def validate_input(variable):
    if variable.isalpha():
        if variable in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            return str(variable)
        else:
            return None
    else:
        return None


lives = 6
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
for char in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guessed_letter = input("Guess a letter: ").lower()
    guess = validate_input(guessed_letter)

    if guess is not None:

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)


        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}. That's not in the word. You lose a life!")

            if lives == 0:
                game_over = True

                print(f"***********************IT WAS '{chosen_word}'!YOU LOSE**********************")

        if guess in correct_letters:
            print(f"You've already guessed {guess}")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN!****************************")

        if lives > 0:
            print(hangman_art.stages[lives])


    else:
        print('Invalid Input. Please enter an alphabet to guess.')
