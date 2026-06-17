import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
print("Welcome to the Python Rock-Paper-Scissors Game!")
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n")

if user_choice.isdigit():
    if user_choice in [0, 1, 2]:
        print(rps[user_choice])

        comp_choice = random.randint(0, 2)
        print(f"Computer choice: {comp_choice} \n{rps[comp_choice]}")

        if comp_choice == 0 and user_choice == 2:
            print("Computer won.")
        elif comp_choice == 2 and user_choice == 0:
            print("You won!")
        elif comp_choice == user_choice:
            print("That's a draw.")
        elif comp_choice > user_choice:
            print("Computer won.")
        elif comp_choice < user_choice:
            print("You won.")

    else:
        print("Invalid Input. Game Over.")
else:
    print("Invalid Input. Game Over.")
