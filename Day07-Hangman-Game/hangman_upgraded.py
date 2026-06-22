import random, hangman_art, hangman_words


def validate_input(variable):
    if variable.isdigit():
        return None
    elif variable.isalpha():
        return variable.lower()
    else:
        return None


def read_game_memory():
    with open("Hangman Gamer Accounts.txt", "a+") as f:
        f.seek(0)
        data = f.readlines()
        each_user = []
        if data == []:
            return each_user
        else:
            for stats in data:
                if stats is '':
                    user, win_number, loss_number = stats.split(',')
                    user = user.strip()
                    win_number = win_number.strip()
                    loss_number = loss_number.strip()
                    each_user.append([user, win_number, loss_number])
            return each_user


def reconstruct_gamer_info(users_list):
    game_memory = {}
    for user in users_list:
        u_name = user[0]
        num_wins = int(user[1])
        num_losses = int(user[2])
        game_memory[u_name] = {'wins': num_wins, 'losses': num_losses}
    return game_memory


def get_stats(username, user_dict):
    if username in user_dict.keys():
        win_num = int(user_dict[username]['wins'])
        loss_num = int(user_dict[username]['losses'])
        if loss_num != 0 or win_num != 0:
            win_percentage = round((win_num / (win_num + loss_num)) * 100, 2)
            print(f"""Your current stats:
Wins: {win_num}
Losses: {loss_num}
Win percentage: {win_percentage}%""")
        else:
            print(f"""Your current stats:
Wins: {win_num}
Losses: {loss_num}
Win percentage: N/A""")


def login_signup(user_dict):
    input_name = input("Please enter your name: ")
    name = title_casing(input_name)
    if name is not None:
        if name in user_dict:
            print(f"Welcome back {name}!")
            get_stats(name, user_dict)
        else:
            user_dict[name] = {'wins': 0, 'losses': 0}
            print(f"Welcome {name}! Let's play our first game!")
            get_stats(name, user_dict)
        return name, user_dict
    else:
        continue_asking = True
        while continue_asking:
            print("Invalid Input. Try Again.")
            input_name = input("Please enter your name: ")
            name = title_casing(input_name)
            if name is not None:
                if name in user_dict:
                    print(f"Welcome back {name}!")
                    get_stats(name, user_dict)
                else:
                    user_dict[name] = {'wins': 0, 'losses': 0}
                    print(f"Welcome {name}! Let's play our first game!")
                    get_stats(name, user_dict)
                continue_asking = False
            else:
                continue_asking = True
        return name, user_dict


def title_casing(variable):
    words = variable.split()

    if len(words) == 0:
        return None

    for word in words:
        if not word.isalpha():
            return None

    return variable.title()


def update_game_memory(updated_dict):
    with open("Hangman Gamer Accounts.txt", "w+") as f:
        for i in updated_dict.keys():
            username = i
            wins = str(updated_dict[username]['wins'])
            losses = str(updated_dict[username]['losses'])
            line = f"{username}, {wins}, {losses}"
            f.write(f"{line}\n")


def hangman_game(username, user_dict):
    lives = 6
    win_num = int(user_dict[username]['wins'])
    loss_num = int(user_dict[username]['losses'])
    print(hangman_art.logo)

    chosen_word = random.choice(hangman_words.word_list)

    placeholder = ""
    for char in chosen_word:
        placeholder += "_"
    print("Word to guess: " + placeholder)

    game_over = False
    correct_letters = []
    guessed_letters = []

    while not game_over:

        print(f"****************************{lives}/6 LIVES LEFT****************************")
        letter_guessed = input("Guess a letter: ")
        guess = validate_input(letter_guessed)

        if guess is not None:

            display = ""

            if guess in guessed_letters:
                print(f"You've already guessed {guess}")
            else:
                guessed_letters.append(guess)

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

                        print(f"***********************IT WAS '{chosen_word}'"
                              f"!YOU LOSE**********************")
                        print(hangman_art.stages[lives])
                        loss_num += 1
                        user_dict[username] = {'wins': win_num, 'losses': loss_num}
                        get_stats(username, user_dict)
                        update_game_memory(user_dict)
                        break

                if "_" not in display:
                    game_over = True
                    print("****************************YOU WIN*****************************")
                    win_num += 1
                    user_dict[username] = {'wins': win_num, 'losses': loss_num}
                    get_stats(username, user_dict)
                    update_game_memory(user_dict)
                    break

                if lives > 0:
                    print(hangman_art.stages[lives])
        else:
            print("Invalid Guess. Please try guessing an alphabet")


gamer_list = read_game_memory()
gamer_dict = reconstruct_gamer_info(gamer_list)
gamer_name, updated_gamer_dict = login_signup(gamer_dict)
hangman_game(gamer_name, updated_gamer_dict)
