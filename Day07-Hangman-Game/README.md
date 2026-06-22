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

## Files in this directory
| File Name                  | Description                                                                               |
|----------------------------|-------------------------------------------------------------------------------------------|
| main.py                    | Contains the simpler version of the game, completed in accordance with the course content |
| hangman_upgraded.py        | Contains the upgraded version of the game with completely independent implementation      |
| hangman_art.py             | Contains the ASCII art for the different stages in the game, and the game logo            |
| hangman_words.py           | Contains the word list for the game                                                       |
| Hangman Gamer Accounts.txt | Is a text file that contains user data for game login option                              | 

## Features in the Original Version (main.py)
* Random word selection
* six-life hangman system
* Visual hangman stages
* Hidden word display using placeholders
* Letter-by-letter guessing
* Correct letter tracking
* Repeated guess warning
* Win/loss condition detection

## Features in Upgraded Version (hangman_upgraded.py)
* Prevent repeated guesses from deducting lives
* Input validation
* Login/Sign-up to the game to store player data
* Score tracking across multiple games
* Persistent player accounts using a text file
* Automatic account creation for new players
* Display player stats before and after each gameplay.
* Win percentage calculation
* Case-insensitive input handling
* Support for multi-word usernames during sign-up/login
* Handles empty account files without crashing

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
