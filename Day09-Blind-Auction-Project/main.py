import os, art

print(art.logo)


def auction():
    winning_bid = 0
    winner_name = ''
    for player in auction_dict:
        if auction_dict[player] > winning_bid:
            winning_bid = auction_dict[player]
            winner_name = player

    print(f"{winner_name} is the winner with a bid of ${winning_bid}")


auction_dict = {}
should_continue = True
while should_continue:
    ask_name_again = True
    while ask_name_again:
        user_name = input("Enter name of bidder: ")
        if user_name == '' or user_name == '\n':
            ask_name_again = True
        else:
            ask_name_again = False

    ask_bid_again = True
    while ask_bid_again:
        bid_amount = input("Enter bidding amount: $")

        if bid_amount.isdigit():
            bid_amount = int(bid_amount)
            if bid_amount < 0:
                ask_bid_again = True
                print("Invalid Input. Please enter a positive integral bid amount.")
            elif bid_amount == 0:
                ask_bid_again = True
                print("Bid amount should be an integer greater than zero. ")
            else:
                ask_bid_again = False

        else:
            print("Invalid Input. Please enter a positive integral bid amount.")
            ask_bid_again = True

    auction_dict[user_name] = bid_amount
    ask_again = True
    while ask_again:
        new_bid = input("Are there any other bidders? Type 'y' for yes and 'n' for no: \n").lower()
        if new_bid not in ['y', 'n']:
            print("Invalid Input. Please try again.")
            ask_again = True

        else:
            if new_bid == 'n':
                should_continue = False
                ask_again = False
                auction()

            else:
                os.system("cls")     #for Windows
                #os.system("clear")  #for Linux/MacOS
                should_continue = True
                ask_again = False
