# Day 17 - Quiz Game
Author: Vindhya Hasini

## Description
This program is a command-line True/False Quiz Game built in Python.

The game represents a series of True/False questions, validates user input, keeps the user's score in track throughout 
the quiz, and displays detailed analysis of performance stats at the end.

While based on the course content, I expanded the application with additional features to improve overall user-experience
and make the game more interactive.

## Files in this directory
| File Name             | Description                                                                                             | Status      |
|-----------------------|---------------------------------------------------------------------------------------------------------|-------------|
| main.py               | Contains the code for the first upgrade of the OOP version of the Quiz Game                             | ✅ Completed |
| data.py               | Contains a list of question dictionaries with respective answers and other crucial info                 | ✅ Completed |
| question_model.py     | Contains the Question class definition and its respective attributes                                    | ✅ Completed |
| quiz_brain.py         | Contains the QuizBrain class definition with respective attributes and methods required for program run | ✅ Completed |
| procedural_version.py | Contains the code for the procedural programming implementation of the program                          | ✅ Completed |

## Concepts Learned
* Object-Oriented-Programming 
* Custom class definitions
* Associating attributes and methods to a class
* Creating objects from a class
* Initializers (__init__)
* Object interaction
* Lists and dictionaries
* 'for' and 'while' loops
* Using the PrettyTable module
* Calculating and displaying game stats
* Randomization of items in a list through the random module
* Modular programming across multiple files

## Features in First Upgraded Version (main.py)
* Interactive True/False quiz
* Randomized order of question across different runs
* Question counter to let the user know how many questions are left
* Live score-tracking after every question
* Input validation to accept only 'True' or 'False' inputs from the user
* Immediate feedback after each question is answered
* Displays the correct answer when the user answers incorrectly
* Final stats table showing:
  * Final Score
  * No.of correctly answered questions
  * No.of incorrectly answered questions
  * Accuracy percentage
* End-of-game performance message based on the player's accuracy

## Future Improvements
* Replay option to restart the game without having to re-run the program
* Persistent high score tracking using file handling
* Player profiles and game history
* Timed quiz mode
* Multiple quiz categories
* Multiple difficulty levels
* Fetching live questions from an online trivia API

## Key Takeaways
* Separating responsibilities between classes makes code easier to understand and maintain
* Input validation prevents unexpected program crashes
* Tiny improvements in the terminal can significantly improve a command-line application
* Building on teh existing project allowed me to practice extending code instead of recreating it

## Challenges Faced
One of the most challenging tasks was to create class definitions, related attributes and methods from scratch. This task 
needed me to map out the possible algorithms for the program run before writing any code.

Designing additional features without disrupting the original code was another challenge I faced.

I also spent time improving the user-experience by validating inputs, organizing final results, formatting terminal output, 
and ensuring the quiz kept tracking the user's score, while maintaining easy-to-manage code.

I also had to encounter many unexpected issues while integrating new features, reinforcing the importance of testing individual 
parts of the program to find where the bug originates from.

## Note
This program was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All upgrades and future improvements are independent implementations
