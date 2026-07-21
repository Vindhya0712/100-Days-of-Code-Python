# Day 25 - US States Game
Author: Vindhya Hasini

## Description
An interactive Python game built using the Turtle Graphics Module and the Pandas Library, where players test their
knowledge by guessing all 50 states in the US. This project is enhanced over the course content with independent implementations.

Each correct guess is displayed at its corresponding location on the map while the score updates in real time. The game
continues until all states are guessed correctly.

## Files in this directory
| File/Folder Name     | Description                                                                                               | Status      |
|----------------------|-----------------------------------------------------------------------------------------------------------|-------------|
| main.py              | Contains the code for the US States Game program by integrating multiple objects and classes              | ✅ Completed |
| 50_states.csv        | Contains the states names, and their respective x and y coordinates on the map chosen                     | ✅ Completed |
| blank_states_img.gif | Contains an image of the US map that acts as the background for the game                                  | ✅ Completed |
| scorecard.py         | Contains the class and method definition for maintaining and updating the user's score                    | ✅ Completed |
| turtle_writer.py     | Contains the class and method definitions that write the state name at its respective position on the map | ✅ Completed |
| game_assets          | A folder that contains images of the game and other data required for the game                            | ✅ Completed |


## Concepts Learned
* Reading CSV Files using the Pandas library
* Working with DataFrames and Series
* Filtering DataFrames based on specific conditions
* Retrieving data from filtered DataFrames
* Converting DataFrame columns into Python lists
* Accessing individual values from a Pandas series
* Displaying images using Turtle Graphics module
* Collecting user input with the textinput() method from the Turtle Graphics module
* Applying OOP by separating responsibilities into different classes
* Managing game state using lists and conditional logic
* Updating graphical interfaces dynamically based on user interaction
* Combining external datasets with graphical applications to create interactive programs


# Features
* Interactive US map using Turtle Graphics
* CSV data handling with Pandas
* Text input for state guesses
* Correct answers displayed on the map
* Live score tracking
* Duplicate answer detection
* OOP design with separate classes for:
  * Scoreboard -- Maintain and update the user's score
  * Turtle Writer -- write the names of correctly guessed states at their respective positions
* Uses DataFrames and Series for coordinate mapping
* Multiple ways to quit the game -- supported via typing 'quit' or clicking the Cancel button in the dialog box
* Lists the states the user failed to guess
* Accuracy percentage and final score are displayed on game end

## Future Improvements
* Create an India States Game using the same architecture
* Introduce different difficulty level -- timed quiz, limited guesses, etc
* Generate a CSV file containing all missed states when the player quits or runs out of time
* Improve label positioning for smalled East Coast states to improve readability
* Make state name matching more flexible by handling short-forms and minor typos in the spellings
* Add persistent high score tracking using file handling
* Upgrade the interface by adding buttons instead of text prompts using Tkinter

## Key Takeaways
This project helped me gain hands-on experience with:
* Reading CSV files using the Pandas library
* Working with DataFrames and Series, and learn some of their methods
* Filtering rows of data based on user's input
* Extracting values from DataFrames
* Combining data analysis with graphical applications
* Separating responsibilities among classes by using an OOP design
* Using the Cancel button to perform an action in main.py

## Challenges Faced
The main challenge I faced while coding this game was the fact that I was working with the Pandas library for the first time.
I had to spend a lot of time reading the documentation, understanding logic and exploring examples online. However, all
this effort helped me expand my knowledge to one of the most useful Python libraries.

Another major challenge I faced was when I decided to add a 'quit' option to the game. I figured it out quite easily, but 
the main challenge came up when I accidentally clicked the Cancel button and caused a program crash. This unprecedented 
bug helped me add another feature to my project -- 'Multiple ways to quit the game'. It taught me that testing edge cases
is just as important as testing code functionality.

## How to play?
1. Clone the repository
2. Navigate to the project folder
3. Install Pandas (ignore if already installed)
4. Run main.py file
5. Enter the name of a US State
6. Correct guesses appear on the map
7. Score is increased by one
8. Duplicate guesses are ignored
9. Guess all 50 states to complete the game
10. Type 'quit' or just use the Cancel button to finish the game

## Preview
* Game start-up screen

![US_States_Game](game_assets/game%20startup%20screen.png)

* End-of-Game screen

![US_States_Game](game_assets/game%20end%20screen.png)

## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All future upgrades will be independent implementations