# Day 19 - Turtle Race Game
Author: Vindhya Hasini

## Description
### main.py
The Turtle Race Game is a graphical Python project built using the Turtle Grpahics module. 
Before the race begins, the player places a bet by predicting which colored turtle will win the race. Once the race starts, 
each color turtle moves forward by a random distance, making the race's outcome unpredictable.

This project introduced me to working with multiple Turtle objects, methods and instances, object lists, randomness, user
interaction through graphical input dialogs and event listeners.

### Etch-a-Sketch-App.py
This program was designed as a coding challenge as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro 
Bootcamp.

This program allows the user to make sketches on the Turtle Graphics window using A, S, D and W keys. Once done, the user
can use the C key to clear all drawings and reset turtle position to start a new set of drawings.

Due to relevance of topics in both programs, I decided to place them in the same directory.

## Files in this directory
| File Name            | Description                                          | Status      |
|----------------------|------------------------------------------------------|-------------|
| main.py              | Contains code for the Turtle Race Game               | ✅ Completed |
| Etch-a-Sketch-App.py | Contains code for the Etch-a-Sketch coding challenge | ✅ Completed |

## Concepts Learned
* Creating and managing multiple Turtle objects
* Creating and managing multiple object instances
* Using lists to iterate through objects and instances
* the random module
* the turtle module
* Graphical user input using the screen.textinput() method
* Object position controlling using the .goto(), .xcor(), .ycor() methods
* Controlling program flow using loops and conditionals
* Basic input validation for GUI-based programs

## Features in main.py
* Six different colored turtles enter a race across the screen
* User places a bet on the winning turtle before the race begins
* Each turtle moves by a random distance with every iteration
* Race ends automatically when a turtle reaches the end of the screen
* Program announces whether the user's prediction was correct

## My upgrades
* Added input validation for the user's bet
* Modified the graphical input prompt to clearly explain invalid inputs instead of silently asking the user again.
* Accepted user input in a more user-friendly manner by validating against the list of available turtle colors
* Kept the original gameplay while making the UX smoother

## Future Improvements
* Allow user to choose the number of turtles participating in a race
* Let user customize turtle colors
* Add multiple racetracks or race-distances
* Track user stats using file handling
* Add replay functionality without having to restart the program
* Display race results in a formatted statistics table

## Key Takeaways
This project taught me that graphical programs require a different way of thinking compared to console-based programs. 
Instead of focusing only on functions, conditionals and logic, I had to understand multiple turtle module methods and 
functions. In order to tackle this, I had to spend more time with the turtle documentation and example code snippets.
I had to understand how multiple objects and instances can interact with simultaneously and how randomness can be used to 
simulate real-world events.

I also realized the importance of validating inputs even in GUI-programs. A small improvement like input validation can 
significantly improve user experience as well as prevent unexpected program crashes.

## Challenges Faced
* Since this was my first GUI-program and the first program working with the turtle module, I needed to spend a lot of time
understanding the documentation to filter methods/functions that might be useful for my project.

* Visualizing game logic before implementation was definitely challenging. 

* Implementing input validation despite the limitations of the Turtle Graphics input dialog.

* Thinking in terms of object interactions rather than a simple set of statements, functions and conditionals

## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

This was the first project where I relied heavily on the walkthrough lectures as it was my first time creating a GUI-program.
Although I couldn't design the solution independently at first, I made sure to understand every step of the implementation
and then added my own input validation feature.

The Etch-a-Sketch-App file contains code for a program that is completely independent of the Turtle Race Game. However, 
due to overlapping concepts, it is added in this directory


