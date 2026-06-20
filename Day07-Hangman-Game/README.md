# Day 07 - Hangman Game
Author: Vindhya Hasini

## Description
This program is a command-line implementation of the classic Hangman Game.
In this game, the player must guess a randomly selected word, one letter at a time, before running out of lives.
The player starts with 6 lives. Each incorrect guess costs a life.
The game ends when:
* The player has guessed all letters correctly while they still have lives (win 🎉)
* All lives are lost (lose ☠️)

The game includes visual hangman stages using ASCII art, life tracking, repeated guess detection and win/loss condition.

## Concepts Learned
* Python lists
* Strings and string manipulation
* 'for' loops and 'while' loops
* Conditional statements
* the random module
* Importing custom modules
* Variable scope
* Game logic implementation
* ASCII art integration

## Features
* Random word selection
* six-life hangman system
* Visual hangman stages
* Hidden word display using placeholders
* Letter-by-letter guessing
* Correct letter tracking
* Repeated guess warning
* Win/loss condition detection

## Future Improvements
* Prevent repeated guesses from deducting lives
* Input validation
* Difficulty levels
* Category-based word selection
* Score tracking across multiple games
* Option to replay without re-starting the program

## Key Takeaways
* Learned how to manage game state using variables and loops
* Practiced tracking user progress throughout the game
* Improved understanding of lists and strings
* Learned how multiple Python modules can work together in a single project
* Gained experience building a complete interactive command-line game
* Strengthened problem-solving skills

## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

The word list and ASCII art required for the game are stored in separate modules with corresponding identifiable file names
to improve code organization and readability.

This project represents my first complete command-line implementation of a game in Python.
