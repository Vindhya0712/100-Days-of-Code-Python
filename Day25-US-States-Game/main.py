from turtle import Screen
import pandas as pd
from scorecard import Scoreboard
from turtle_writer import TurtleWriter

states_dataset = pd.read_csv('game_assets/50_states.csv')
states = states_dataset['state'].to_list()

screen = Screen()
screen.title("Vindhya's US States Game")
screen.bgpic('game_assets/blank_states_img.gif')
screen.tracer(0)

scorecard = Scoreboard()
turtle_writer = TurtleWriter()

user_answers = []

while scorecard.score < 50:
    screen.update()
    user_input = screen.textinput(title='States Game', prompt=f"Guess the state: \n(Type 'quit' or click Cancel to finish the game) ")

    if user_input is None:
        print("You quit the game.")
        print("Missed States: \n")
        for state in states:
            if state not in user_answers:
                print(f"{state}")
        break

    else:
        user_input = user_input.strip().title()
        if user_input in states:
            if user_input in user_answers:
                print(f"Already guessed {user_input}")
            else:
                scorecard.score += 1
                user_answers.append(user_input)
                state_deets = states_dataset[states_dataset.state == user_input]
                xcor = state_deets['x'].iloc[0]
                ycor = state_deets['y'].iloc[0]
                turtle_writer.write_state_name(xpos=xcor, ypos=ycor, state_name=user_input)
                scorecard.update_score()

        elif user_input == 'Quit':
            print(f"You quit the game.")
            print("Missed States: \n")
            for state in states:
                if state not in user_answers:
                    print(f"{state}")
            break

accuracy = round((scorecard.score / 50) * 100, 2)
print(f"\nYour final score: {scorecard.score} \nAccuracy: {accuracy}%")
screen.exitonclick()
