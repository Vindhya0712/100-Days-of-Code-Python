# Day 08 - Caesar Cipher Project
Author: Vindhya Hasini

## Description
This implements the Caesar Cipher, a simple encryption technique that shifts alphabetical characters by a specified 'shift number'.

The program supports both encoding and decoding messages while preserving upper/lower case of alphabets, special characters, spaces and numbers.
It also provides statistics about the encoding/decoding process.

## Files in this directory
| File Name                 | Description                                                                    | Status      |
|---------------------------|--------------------------------------------------------------------------------|-------------|
| main.py                   | Contains code for the basic version of the project                             | ✅ Completed |
| art.py                    | Contains ASCII art to improve user experience on startup                       | ✅ Completed |
| caesar_cipher_upgraded.py | Contains code for the upgraded version of the project with additional features | ✅ Completed |

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

## Features in Original Version(main.py)
* Supports both uppercase/lowercase alphabets
* Supports custom shift number
* Character shift wrapping using modulo 
* Preserves spaces, special characters and numbers during encryption/decryption
* Interactive and easy to use menu-driven interface
* Encryption/Decryption stats:
  * No.of characters encoded/decoded
  * No.of spaces preserved
  * No.of numbers preserved
* Exit option for terminating the program run
* Supports repeated program runs without having to restart the program

## Features in the Upgraded version (caesar_cipher_upgraded.py)
* Input validation for menu choices and shift number
* Save encryption history to text file
* View previously encoded/decoded messages

## Future Improvements
* Allow users to clear stored history
* Display total encryptions/decryptions

## Key Takeaways
* Learned how to classical Caesar Cipher encoding system works
* Practiced working with lists and strings
* Improved understanding of functions, parameters and arguments
* Learned how the modulo operator can be used for cyclic operations
* Strengthened problem-solving skills by extending the simple program with my own implementations

## Note
This project was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

The upgraded version extends the original course project with additional functionality.

This implementation is extended for educational purposes only and demonstrates the fundamentals of the age-old system of Caesar Cipher. 
