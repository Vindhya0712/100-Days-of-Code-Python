# Day 14 - Higher Lower Game
Author: Vindhya Hasini

## Description
This project is a Python implementation of the Higher Lower game. 

In this game, the player is presented with two public figures and asked to guess which one of them has more followers on 
Instagram. Every correct guess increases the score, while one incorrect guess ends the game.

## Files in this directory
| File Name    | Description                                                                                                                     | Status      |
|--------------|---------------------------------------------------------------------------------------------------------------------------------|-------------|
| main.py      | Contains code the first upgraded version of the course content                                                                  | ✅ Completed |
| game_data.py | Contains the list of public figures, their occupations, their native country and the number of followers they have on Instagram | ✅ Completed |
| art.py       | Contains ASCII art to make the game more interactive by enhancing user experience                                               | ✅ Completed |

## Concepts Learned
* Functions
* the random module
* Conditionals
* 'for' and 'while' loops
* Dictionaries and nested data structures
* Importing from other Python files
* Managing program state across the implementation
* Tracking user's score across the game
* Breaking a larger problem into simpler functions

## Features
### Features in the Original Version (based on course content)
* Interactive command-line gameplay
* Random celebrity comparisons every round
* Continuous score tracking 
* Console-clearing between rounds for a cleaner user experience
* Re-use of winning option in the next comparison

### Features in the first upgrade (main.py)
* Input validation throughout the game
* Prevention of duplicate comparisons by ensuring that two randomly selected celebrities are always different
* Option to play again without having to restart the program

### Future Improvements
* Multiple difficulty levels
* User login/sign-up option
* Persistent game stats
* Highest score tracking for a certain user through file handling
* Date and timestamp for every game
* Display user's stats(wins, losses, win%)
* PrettyTable formatting
* Better UI and messages

## Key Takeaways
Although the game itself is straightforward, building it required careful thinking about program flow and state management
Some valuable lessons from the project include:
* Solving the problem is not the only part of programming -- organizing the solution is equally important
* Writing functions that each perform a single responsibility makes code easier to read and manage
* Managing data between game rounds requires careful planning
* Input handling prevents unexpected program crashes
* Readable and modular code becomes increasingly important as projects grow

## Challenges Faced
* Carrying over the winning guess to the next round 
* Trying to prevent program crash by ensuring that the two randomly selected celebrities are always different
* Designing the program to have readable code while ensuring robust features was definitely a valuable lesson

## Note
This program was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All upgrades and future improvements are independent implementations
