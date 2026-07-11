# Day 24 - Mail Merge Project
Author: Vindhya Hasini

## Description
A Python automation project that generates personalized letters by reading given names from a text file and modifying
the placeholder name in the letter template.

## Files in this directory
| Folder/File Name                  | Description                                                                            | Status      |
|-----------------------------------|----------------------------------------------------------------------------------------|-------------|
| Input                             | A folder that contains 2 sub-folders holding the letter template and names of invitees | ✅ Completed |
| Input/Letters/starting_letter.txt | A text file that contains the letter template                                          | ✅ Completed |
| Input/Names/invited_names.txt     | A text file that contains names of invitees on separate lines                          | ✅ Completed |
| Output/ReadyToSend                | A folder that contains the personalized letters for each of invitees as text files     | ✅ Completed |
| main.py                           | Contains the Python code that completes this project                                   | ✅ Completed |

## Project Structure

Day-24-Mail-Merge-Project

    Input

        Letter

            starting_letter.txt

        Names

            invited_names.txt

    Output

        ReadyToSend

            letter_for_Vindhya.txt

            letter_for_Hasini.txt

    main.py

    README.md

## How to Run
1. Clone this repository
2. Open the project in preferred Python IDE
3. Add or edit names inside:

Input/Names/invited_names.txt
4. Edit the letter template inside:

Input/Letter/starting_letter.txt

5. Run

main.py

6. Personalized invitation letters will automatically be generated inside:

Output/ReadyToSend/

## Concepts Learned
* File Handling for text files
* Opening files manually and using the 'with' keyword
* Absolute and Relative File Paths
* Dynamic File Names and Paths
* Dynamic File Creation
* Different modes while opening files
* .read(), .readlines() methods for reading from a text file
* .write() for writing into a text file
* Python lists and list traversing
* Python dictionaries and dictionary manipulation
* string methods -- f-strings, .strip() and .replace() 
* Loops

## Features
* Read a list of invitees from invited_names.txt
* Read a letter template containing a placeholder name (here, '[name]')
* Generate a personalized letter for everyone in invited_names.txt
* Automatically creates a uniquely named text file for each recipient
* Saves all generated text files to Output/ReadyToSend folder

## Future Improvements
* Support multiple placeholders like -- [date], [time] and [venue]
* Allow users to provide invitee details using CSV files
* Add support for personalized email generation
* Build a simple GUI version using Tkinter
* Export invitations as PDF files
* Add login system to display how many successful generations happened previously
* Allow users to choose custom Output folders
* Provide user-friendly error messages

## Key Takeaways
* Clean file input using .strip() and .replace() methods
* Generating multiple files automatically
* Working with multiple folders in the same repository
* Decide which files to add to .gitingore
* Understanding dynamic file name generation and file creation

## Challenges I Faced
One of the major challenges I faced was creating personalized file names for each recipient. However, by doing some
research online, I found out that we can create files by using dynamic file names instead of static ones. 
Hence, I took this idea further, and implemented it using dictionaries independently.

Implementing this whole project without watching the walkthrough lectures was definitely one of my biggest achievements.

## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All future upgrades will be independent implementations

