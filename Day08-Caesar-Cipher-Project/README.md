# Day 08 - Caesar Cipher Project
Author: Vindhya Hasini

## Description
This implements the Caesar Cipher, a simple encryption technique that shifts alphabetical characters by a specified 'shift number'.

The program supports both encoding and decoding messages while preserving upper/lower case of alphabets, special characters, spaces and numbers.
It also provides statistics about the encoding/decoding process.

## Files in this directory
| File Name                 | Description                                                                           | Status      |
|---------------------------|---------------------------------------------------------------------------------------|-------------|
| main.py                   | Contains code for the first upgraded version of the basic course project              | ✅ Completed |
| art.py                    | Contains ASCII art to improve user experience on startup                              | ✅ Completed |
| caesar_cipher_upgraded.py | Contains code for the second upgraded version of the project with additional features | ✅ Completed |

## Concepts Learned
* Python lists
* Functions
* Parameters and arguments
* Conditional statements
* Loops
* String manipulation
* Modulo operator (%)
* User input handling
* String methods like .islower(), .isalpha(), .isupper()
* the datetime module
* Methods in datetime module like .strftime() and .now()
* the PrettyTable module

## Features

### Original Project (Based on course content)
* Encode text
* Decode text
* Custom shift values

### Upgrade 1.0 (main.py)
* Supports both uppercase and lowercase alphabets
* Character wrapping using modulo arithmetic
* Preserves spaces, numbers and special characters while encoding/decoding
* Menu-driven interface
* Encryption/Decryption stats
* Repeated program runs without having to re-run the project
* Exit option

### Upgrade 2.0 (caesar_cipher_upgraded.py)
* Robust input validation
* View current session history
* Save current session history to a text file
* Persistent history across multiple program runs
* Duplicate-entry prevention
* PrettyTable formatting for saved history
* Date and time stamps for every saved entry

## Future Improvements
* Allow users to clear stored history
* Display total encryptions/decryptions

## Key Takeaways
* Learned how to classical Caesar Cipher encoding system works
* Practiced working with lists and strings
* Improved understanding of functions, parameters and arguments
* Learned how the modulo operator can be used for cyclic operations
* Learned to work with strftime() from the datetime module
* Learned basic OOP to work with PrettyTable
* Strengthened problem-solving skills by extending the simple program with my own implementations

## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All upgraded versions and upcoming improvements are independent implementations
