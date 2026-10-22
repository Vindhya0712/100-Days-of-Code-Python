# Day 28 - Pomodoro Timer App
Author: Vindhya Hasini


## Description
A Pomodoro Timer App built using Python and Tkinter to support focused work sessions and scheduled breaks. The
application automatically switches between  work and break intervals while tracking completed work sessions.

## Files in this directory
| File Name   | About                                                                             | Status       |
|-------------|-----------------------------------------------------------------------------------|--------------|
| main.py     | Contains the complete code for the application                                    | ✅ Completed |
| game_assets | A folder that contains the images used in the app and the README for this project | ✅ Completed |

## Concepts Learned
* Tkinter GUI development
* Creating and organizing Tkinter widgets
* Event handling
* Timer functionality -- countdown and reset logic using the after() method
* Time conversion and formatting the display using dynamic typing
* Functions and state management
* Conditional logic

## Features
* A countdown timer that displays the remaining time in minutes and seconds
* A start button that initiates the timer
* A reset button to reset the timer and clear the current session progress
* Runs focused work sessions of 25 minutes
* Automatically schedules short breaks of 5 minutes each after a successful work session
* Provides a 20 minute 'long break' on completing 4 work sessions
* A session tracker displays the number of pomodoros completed

## Future Upgrades
* Customizable timer modes
* Ultradian sprint mode (90min work with 10min break)
* Customizable themes with alternative visuals
* Desktop notifications
* Productivity stats
* Persistent settings

## Key Takeaways
* Learned how to implement countdown timers in Tkinter without blocking the GUI's event loop
* Gained experience coordinating timer logic, GUI updates, and session transitions
* Understood how functions, conditional statements, and counters work together to manage the application's state
* Improved understanding of event-driven programming

## Challenges Faced
One of the major challenges I faced while building this project was to figure out how to create a countdown functionality
without affecting a GUI's event loop. Solving this problem helped me understand the after() method and its uses.

Another major problem I faced was in implementing the timer reset logic. Figuring this out needed me to explore the new
methods like after_cancel().

This project marks my first application, and it was definitely a new experience and I had to rely a lot on the lectures 
unlike all the previous projects I tackled with

## Preview
This is how the app looks upon opening
![App Open page](Day28-Pomodoro-Timer-App/game_assets/pomodoro start page.png)


This is how a work session on the app looks like
![Work Session](Day28-Pomodoro-Timer-App/game_assets/pomodoro open page.png)

This is how a short break looks like on the app
![Short Break Session](Day28-Pomodoro-Timer-App/game_assets/pomodoro break page.png)

## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp course.

All future upgrades will be independent implementations.
