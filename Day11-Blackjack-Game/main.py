import random, art, os

def blackjack_game():
    def boot_game():
        os.system("cls")
        print(art.logo)
        game()
        play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if play_again.isalpha():
            if play_again == 'y':
                boot_game()
            else:
                print("Goodbye! 👋")
        else:
            print("Invalid Input. Game Exiting.")

    def deal():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        card = random.choice(cards)
        return card

    def blackjack_check(hand):
        if sum(hand) == 21 and len(hand) == 2:
            return 100

    def is_busted(hand):
        if sum(hand) > 21:
            return 0

    def adjust_ace(hand):
        if 11 in hand and sum(hand) > 21:
            index_ace = hand.index(11)
            hand[index_ace] = 1

    def dealer_cards(c_hand):
        while sum(c_hand) < 17:
            c_hand.append(deal())
            adjust_ace(c_hand)
        return c_hand, sum(c_hand)


    def compare_scores(p_score, c_score):
        while p_score < 21 and c_score < 21:
            if c_score == 21 and p_score != 21:
                return "Computer Wins. 😭"
            elif c_score != 21 and p_score == 21:
                return "You Won! 😁"
            elif p_score == c_score:
                return "That's a draw. 🫠"
            elif p_score > c_score:
                return "You Won! 😁"
            elif c_score > p_score:
                return "Computer Wins. 😭"
        return None

    def game():
        player_hand = []
        comp_hand = []
        for i in range(2):
            player_hand.append(deal())
            comp_hand.append(deal())

        adjust_ace(player_hand)
        player_score = sum(player_hand)
        if player_score > 21 and 11 in player_hand:
            adjust_ace(player_hand)
        player_score = sum(player_hand)

        adjust_ace(comp_hand)
        comp_score = sum(comp_hand)
        if comp_score > 21 and 11 in comp_hand:
            adjust_ace(comp_hand)
        comp_score = sum(comp_hand)

        continue_game = True
        while continue_game:
            bj_check = blackjack_check(comp_hand)
            if bj_check == 100:
                continue_game = False
                print(f"Your final hand: {player_hand}, Your final score: {sum(player_hand)}")
                print(f"Computer's final hand: {comp_hand}, Computer's final score: {comp_score}")
                print("Computer won by BlackJack! 😭")
                break

            bj_check = blackjack_check(player_hand)
            if bj_check == 100:
                continue_game = False
                print(f"Your final hand: {player_hand}, Your final score: {sum(player_hand)}")
                print(f"Computer's final hand: {comp_hand}, Computer's final score: {comp_score}")
                print("You won by BlackJack! 😎")
                break

            print(f"Your current hand: {player_hand}, Your current score: {player_score}")
            print(f"Dealer's first card: {comp_hand[0]}")
            ask_again = True
            while ask_again:
                hit_stand = input("What do you wanna do?\n"
                                  "1. Hit\n"
                                  "2. Stand\n"
                                  "Type the number against your choice: ")

                if hit_stand.isdigit():
                    hit_stand = int(hit_stand)
                    if hit_stand == 1 or hit_stand == 2:
                        if hit_stand == 1:
                            player_hand.append(deal())
                            adjust_ace(player_hand)
                            player_score = sum(player_hand)
                            bust = is_busted(player_hand)
                            if bust == 0:
                                ask_again = False
                                continue_game = False
                                print(f"Your final hand: {player_hand}, Your final score: {player_score}")
                                print(f"Computer's final hand: {comp_hand}, Computer's final score: {comp_score}")
                                print("You got busted! 😭")
                                break

                            else:
                                print(f"Your current hand: {player_hand}, Your current score: {player_score}")
                        elif hit_stand == 2:
                            ask_again = False
                            print(f"Your final hand: {player_hand}, Your current score: {player_score}")

                    else:
                        print("Invalid Input!")
                else:
                    print("Invalid Input!")

            if continue_game:
                final_comp_hand, final_comp_score = dealer_cards(comp_hand)
                print(f"Computer's final hand: {final_comp_hand}, Computer's final score: {final_comp_score}")
                bust = is_busted(final_comp_hand)
                if bust == 0:
                    print("Computer got busted! 🤣\nYou won!")
                    break

                else:
                    winner = compare_scores(player_score, final_comp_score)
                    print(winner)
                    break

    os.system("cls")
    yes_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if yes_no == 'y':
        boot_game()
    else:
        print("Guess you don't wanna play... 😓")


blackjack_game()