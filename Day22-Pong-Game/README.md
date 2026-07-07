# Day 22 - Pong Game
Author: Vindhya Hasini

## Description
A classic two-player Pong Game built in Python using the Python Turtle Graphics Module.

This project focuses on applying Object-Oriented-Programming (OOP) concepts while designing independent classes for each 
part of the game -- paddles, ball and the scorecard, all while implementing real-time game mechanics such as collision
detection, bounce conditions, scoring and game state management.

## Files in this directory
| File Name     | Description                                                                                                                                                  | Status      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| main.py       | Contains code for all the core game mechanics. It integrates objects created from different classes and gets them to work together for the favorable output. | ✅ Completed |
| paddle.py     | Contains attributes and methods for the Paddle class. It manages the behaviour and movement of the paddle objects                                            | ✅ Completed |
| ball.py       | Contains attributes and methods for the Ball class. It manages the behaviour of the ball -- moving across the screen and bouncing whenever needed            | ✅ Completed |
| scoreboard.py | Contains attributes and methods for the Scoreboard Class. It manages the display and update of the scorecard                                                 | ✅ Completed |
| game_assets   | It is a folder that contains images and video recordings of the game, clearly meant for use in the README                                                    | ✅ Completed |

## Concepts Learned
* Object-Oriented-Programming (OOP)
* Working with multiple interacting objects from different classes
* Attributes and methods 
* Class inheritance
* Turtle Graphics Module
* Keyboard even handling
* Collision detection using object distance
* Coordinate system and object positioning
* Game loop implementation
* Screen animation methods -- tracer() and update()
* Organizing code into multiple modules

## Features
* Two player game
* Two independently controlled paddles
* Smooth ball movement
* Ball bounces off at the top and bottom edges of the screen
* Ball bounces off the paddles
* Automatic score tracking
* Ball resets to center everytime any paddle misses to catch it
* Increment ball speed by 0.9 times every time any paddle catches it
* Paddle movement constrained within the game window
* Classic black-and-white game window to give arcade-style feeling

## Future Improvements
* Add a winning score and display winning message
* Improve paddle-ball collision logic to handle occasional cases of repeated bounces at certain collision angles
* Add sound effects for paddle hits and scoring
* Use retro arcade fonts and visual effects
* Add a start menu and restart option

## Key Takeaways
This project strengthened my understanding of Object-Oriented Programming by showing how multiple independent objects 
can work together to build a complete game.

Compared to previous projects, I became more confident in designing classes before watching the walkthrough and solving 
several implementation challenges independently. Building Pong also improved my understanding of collision detection, 
game loops, object interaction, and event-driven programming.

## Challenges Faced
Some of the main challenges I faced are:
* Designing the paddle class using inheritance from the Turtle() class, instead of creating separate turtle objects
* Understanding how to move the ball diagonally across the screen using the turtle co-ordinate system and x_cor() and
y_cor() methods
* Implementing realistic ball bouncing behaviour
* Coordinating interaction between multiple classes while keeping code organized
* Restricting paddle movements so they don't disappear off the screen

## Gameplay
* Two-player local game
* Left Player: W (up)/ S (down)
* Right Player: ⬆️ (up)/ ⬇️ (down)
* The objective: prevent the ball from going off the screen.
* Scoring System: if a player misses the ball, the opponent scores a point immediately

* Gameplay gif:

![Pong Game](game_assets/pong%20game%20code%20run.gif)

* Game Start-Screen:

![Pong Game](game_assets/pong%20game%20startup%20screen.png)


## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All future improvements will be independent implementations
