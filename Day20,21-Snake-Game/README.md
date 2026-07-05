# Day 20 & 21 - Snake Game
Author: Vindhya Hasini

## Description
A classic Snake Game built in Python using the Python Turtle Graphics module.

This program helped me understand Object-Oriented-Programming (OOP) by organizing my game code into multiple classes and 
modules. It also strengthened my problem-solving skills, as I challenged myself to implement several features before
watching the solution walkthrough.


## Files in this directory
| File Name     | Description                                                                                                                                                   | Status      |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| main.py       | Contains all the code and logic for the snake game by integrating multiple objects created from multiple classes and getting them to work together            | ✅ Completed |
| snake.py      | Contains attributes and methods related to the snake -- creating a snake, increasing its length and controlling its movement                                  | ✅ Completed |
| food.py       | Contains attributes and methods related to the food -- creating pieces and food, and getting them to appear at random locations                               | ✅ Completed |
| scoreboard.py | Contains attributes and methods related to the scorecard -- initializing score to 0, increasing the score, displaying the score on the Turtle Graphics Window | ✅ Completed |
| game_assets   | Contains images and videos related to the output of the code, purely meant for being added to the README                                                      | ✅ Completed |


## Concepts Learned
* Object-Oriented-Programming (OOP)
* Classes and Objects
* Instances of an object
* Class Inheritance
* Python Modules
* Turtle Graphics Module
* Event Listeners
* Binding key-presses with functions
* List slicing
* Code refactoring
* the random module


## Features
* Snake moves smoothly using keyboard controls -- through all the 4 arrow keys
* Food appears at random locations
* Live score-tracking displayed during gameplay
* Snake grows after eating food
* Game ends when:
  * The snake collides with the wall
  * The snake collides with its own tail
* Final score is displayed when the game ends


## Future Improvements
* Persistent high score tracking
* Restart game option
* Multiple difficulty levels
* Special food with bonus points
* Player stats
* Multiple themes


## Key Takeaways
This project was my first larger Python application built over multiple classes.

While building it, I learned how to:
* Design programs using OOP
* Separate different responsibilities into different classes
* Detect collisions with objects -- food and own body
* Use inheritance while creating classes
* Refactor code to improve readability
* Reuse concepts from one part of the program to solve another


## Challenges Faced
The main challenge faced while coding the entire program was maintaining multiple classes and objects

Another challenge was to figure out where to use class inheritances. I needed to visualize the functions of an object 
that can be created from a certain class, its functions, attributes and methods all before writing any code. Although it
was quite challenging, it improved my programming skills and thinking process significantly.

I tried to solve the program in multiple steps before watching the walkthrough. This was challenging in a fun way, and
also accelerating my learning capabilities.

### Personal Highlights
Below are some parts of the program I implemented or improved on my own:
* Created the Scoreboard class by applying concepts learnt while creating the Food class
* Used list-slicing to simplify tail collision detection instead of checking every segment individually
* Refactored portions of the snake creation logic to make the code cleaner and more readable

### Developer Notes
This project marked a turning point in my Python journey. It was my first experience building a larger application using 
multiple classes. I especially enjoyed implementing the scoreboard independently by applying concepts from the Food 
class, and simplifying tail collision detection using Python list slicing.

## Gameplay
![Snake Gameplay](game_assets/snake%20game%20code%20run.gif)

Start-up screen

![Snake Gameplay](game_assets/snake%20game%20startup%20screen.jpg)

Game Over screen

![Snake Gameplay](game_assets/snake%20game%20exit%20screen.jpg)


## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All future improvements will be independent implementations.
