import random, hangman_art, hangman_words

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
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

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

            print(f"***********************IT WAS '{chosen_word}'a"
                  f"!YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    if lives > 0:
        print(hangman_art.stages[lives])
