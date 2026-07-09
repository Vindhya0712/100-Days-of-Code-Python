# Day 23 - Turtle Crossing Game
## ⭐ Capstone Project 2
Author: Vindhya Hasini

## Description
This is a simple arcade-style game built in Python using the Python Turtle Graphics module.

The objective is simple: help the turtle to cross an increasingly busy road without getting hit by moving cars. Every
successful road-cross levels up the difficulty by speeding up the cars.

## Files in this directory
| File Name | Description | Status |
| --------- | ----------- | ------ |
| main.py | Contains the main logic of the game. Integrates multiple objects from different classes for the desired results | ✅ Completed |
| car_manager.py | Creates new cars on the road, moves them and increases their speed when needed | ✅ Completed |
| player.py | Contains attributes and methods related the player (here, the turtle) | ✅ Completed |
| scorebaord.py | Manages the scorebaord, displays current level, levels up when needed, and prints the game over message | ✅ Completed |
| game_assets | A folder that contains a gif of the program run, and pictures of the startup screen and 'game over' screen | ✅ Completed |


## Concepts Learned
* Object-Oriented-Programming (OOP)
* Class Inheritance
* Creating and managing multiple objects
* Lists of objects
* Collision detection
* Event handling with keyboard listeners
* Turtle graphics
* Game loops
* Randomization
* Game state management, balancing and difficulty progression

## Features
* Object-Oriented design with multiple classes
* Independent Player, Scoreboard, and CarManager classes
* Randomly generated traffic
* Increase in game difficulty as level increases
* Collision detection between turtle and cars
* 'Game Over' screen
* Randomly colored cars
### My Enhancements
* Multiple traffic lanes for cleaner and more realistic traffic flow
* Tuned car spawn rate for improved game balance
* Display the player's highest level, in the console, after the game ends

## Future Improvements
* Implement smarter lane-based spawning to prevent cars from appearing too close to each other
* Add left and right movement for the turtle, making navigation more strategic
* Introduce vehicles with varying sizes and speeds into the traffic flow
* Add a persistent high-score system that saves the highest score a user has reached over multiple game sessions
* Gradually increase the traffic spwn rate in addition to increase in vehicle speeds
* Add sound-effects for a more arcade-like experience
* Introduce animated road markings and background scenery to create a more immersive environment


## Key Takeaways
This project significantly improved by OOP understanding.

Some of my biggest takeaways include:
* Designing classes before writing code
* Managing multiple objects
* Making sure that each method in a class has a single responsibility. This helped improve game logic
* Building and maintaining a game loop
* Balancing gameplay by adjusting spawn rates and movement speed
* Improving tutorial project with my own design ideas instead of simply reproducing it

## Challenges Faced
Major challenges faced while coding the game arose when trying to add independent implementations.

* Adding a lane-based traffic system: This was a thought that struck to me after trying multiple ways to avoid overlap of 
cars on the lane (to some extent)

* Balanced car-spawn rates: This feature was developed after experimenting with multiple probabilities to find the 
sweet-spot for a balanced gameplay

* Adjusted car-speed increment: This feature was also included after multiple game runs. It allows the player to feel a 
balanced and progressive increase in car speed, every level.

Some other challenges include:
* Designing the CarManager class
* Managing multiple car objects moving simultaneously
* Implementing random traffic generation
* Creating clean traffic without visual clutter
* Understanding how different classes interact within a game loop

## Gameplay
* Control the turtle using the 'Up Arrow' key ⬆️
* Safely cross the road while avoiding incoming traffic
* Every successful crossing:
  * Resets the turtle to the starting position
  * Increases the game level
  * Increases the speed of incoming cars
* The game ends immediately when the turtle collides with a car
* Gameplay video

![Turtle Crossing Game](game_assets/turtle%20crossing%20code%20run%20gif.gif)

* Game Start-up Screen

![Turtle Crossing Game](game_assets/turtle%20crossing%20startup%20screen.png)

* Game Over Screen

![Turtle Crossing Game](game_assets/turtle%20crossing%20game%20over.png)


## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All personal enhancements and future upgrades will be independent implementations

