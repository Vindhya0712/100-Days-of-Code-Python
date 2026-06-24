# Day 10 - Calculator Project
Author: Vindhya Hasini

## Description
This is an interactive command-line calculator built in Python featuring arithmetic operations, session-based memory storage,
history tracking, error handling, and support for chained calculations.

This calculator supports operations like addition, subtraction, multiplication, division, modulo and power operations

## Files in this directory
| File Name              | Description                                               | Status                                        |
|------------------------|-----------------------------------------------------------|-----------------------------------------------|
| main.py                | Contains the code for the basic version of the program    | ✅ Completed                                   |
| art.py                 | Contains the ASCII art for better user interface          | ✅ Completed                                   |
| calculator_upgraded.py | Contains the code for the upgraded version of the program | ✅ Completed, but there may be future upgrades | 


## Concepts Learned
* Functions
* Using functions as values in a dictionary
* Dictionaries
* Nested functions
* Error-handling with try-except block
* Lists and list operations
* Program state management
* User input validation

## Features in the Original Version (main.py)
* The calculator can perform the following functions:
  * Addition
  * Subtraction
  * Multiplication
  * Division
* Continuous calculations with and/or without the result of the previous calculation

## Features in the Upgraded Version (calculator_upgraded.py)
* The calculator can perform the following functions:
  * Addition
  * Subtraction
  * Multiplication
  * Division
  * Modulo operation
  * Exponentiation
  * Continuous calculations using previous results
* Session-based calculator memory
* Memory recall
* Memory clearing
* Session-based calculator history
* Viewing calculator history
* Calculation counter
* Division-by-zero handling
* Overflow handling

## Future Upgrades
* Persistent memory using text files
* Persistent calculation history
* Scientific calculator functions (sqrt, log, sin, cos, etc.) using the Math module
* GUI version using Tkinter
* OOP version of the program

## Key Takeaways
* Dictionaries can be used to map operators to functions, making code easier to understand and maintain
* Breaking a program into smaller functions improves readability and maintainability of code
* Error handling helps prevent program crashes 
* Features such as memory and history can be implemented using lists
* Sometimes bugs and program crashes reveal loopholes in the program design that give ideas to upgrade the project

## Note
This program was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All upgrades and future improvements are independent implementations
