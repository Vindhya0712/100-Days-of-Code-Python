from turtle import Screen
import pandas as pd
from scorecard import Scoreboard
from turtle_writer import TurtleWriter

states_dataset = pd.read_csv('50_states.csv')
states = states_dataset['state'].to_list()

screen = Screen()
screen.bgpic('blank_states_img.gif')
screen.tracer(0)

scorecard = Scoreboard()
turtle_writer = TurtleWriter()

user_answers = []

while scorecard.score < 50:
    screen.update()
    user_input = screen.textinput(title='States Game', prompt='Guess the state: ').title().strip()
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
            print(f"{user_input} is correct")
    else:
        print(f"{user_input}Wrong")

print(f"Your final score: {scorecard.score}")
print(f'{user_answers}')
screen.exitonclick()
