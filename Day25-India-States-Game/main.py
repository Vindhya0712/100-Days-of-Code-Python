from turtle import Screen
import pandas as pd
from scorecard import Scoreboard
from turtle_writer import TurtleWriter

states_dataset = pd.read_csv('game_assets/states_uts.csv')
states = states_dataset['state_ut'].to_list()

screen = Screen()
screen.title("Vindhya's India States Game")
screen.setup(900, 860)
screen.bgpic('blank_india_map.gif')
screen.tracer(0)

scorecard = Scoreboard()
turtle_writer = TurtleWriter()

user_answers = []

while scorecard.score < 36:
    screen.update()
    user_input = screen.textinput(title='India States Game', prompt=f"Guess the state/UT: \n(Type 'quit' or click Cancel to finish the game) ")

    if user_input is None:
        print("You quit the game.")
        break

    else:
        user_input = user_input.strip().lower()
        if user_input in states:
            if user_input in user_answers:
                print(f"Already guessed {user_input}")
            else:
                scorecard.score += 1
                user_answers.append(user_input)
                state_deets = states_dataset[states_dataset.state_ut == user_input]
                xcor = state_deets['x'].iloc[0]
                ycor = state_deets['y'].iloc[0]
                turtle_writer.write_state_name(xpos=xcor, ypos=ycor, state_name=user_input)
                scorecard.update_score()

        elif user_input == 'quit':
            print(f"You quit the game.")
            break

accuracy = round((scorecard.score / 36) * 100, 2)
if accuracy != 100.00:
    print("States/UTs you missed: \n")
    for state in states:
        if state not in user_answers:
            print(f"{state}")
    print(f"\nYour final score: {scorecard.score} \nAccuracy: {accuracy}%")
else:
    print(f"\nCongratulations! \nYou guessed all 28 States and 8 Union Territories!\n")
    print(f"\nYour final score: {scorecard.score} \nAccuracy: {accuracy}%")
screen.exitonclick()
