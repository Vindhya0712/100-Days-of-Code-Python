# Day 15 - Coffee Machine Project
Author Name: Vindhya Hasini


## Description
PyCoffee is a command-line coffee machine simulator built in Python.

This program allows the user to order coffee, process coin payments, check available resources, dispense drinks and keep 
track of machine's resources and earnings.

While inspired by the original course project, I extended this project with independent implementations to help enhance
the user experience


## Concepts Learned
* Functions and modular programming
* Dictionaries and nested dictionaries
* Conditionals
* 'for' and 'while' loops
* User input validation
* Managing program state
* Update resources after every drink is made
* PrettyTable module


## Features
### Features in the Original Version (based on course content)
* Simple Coffee Menu on startup
* Three available drinks:
  * espresso
  * latte
  * cappuccino
* Check resource availability before purchase
* Coin-based payment system
* Automatic change calculation
* Resource deduction after every successful purchase
* Earnings tracking
* Display resource report on user demand
* Machine shutdown option

### Features in the first upgrade (main.py)
* Interactive Coffee Menu on startup formatted using PrettyTable
* Display formatted machine report using PrettyTable
* Input validation for menu options and coin entries
* 'Retry' or 'Cancel Purchase' options when the user enters insufficient money
* User-friendly messages with emojis
* Better terminal experience

### Future Improvements
* Persistent resource storage using file handling
* Admin mode for refilling ingredients
* Multiple drink sizes (small, medium and large)
* Order history
* Daily sales report
* More beverages/seasonal drinks
* OOP version of the Coffee Machine


## Key Takeaways
* Dividing a larger program into smaller, more focused functions improves functionality and readability
* Input validation greatly improves user experience and prevents unexpected program crashes
* Separating responsibilities among functions reduces the chances of duplicate logic being a part of the program
* Small improvements to terminal experience can make command-line projects feel more polished
* Tracking shared resources across different parts of the program requires careful planning


## Challenges Faced
One of the major challenges I faced was to figure out the program flow for the Coffee Machine while limiting the responsibility
of each function down to only one task.

Managing resources, validating user inputs, handling different payment scenarios, and ensuring all associated variables 
update correctly after every drink dispensal was quite challenging.

Another major challenge I faced was making the program more user-friendly rather than simply functional. Adding formatted
tables, input validation, clearer error-messages, and retry/cancel options helped create a smooth user-experience while
keeping the codebase organized.


## Note
This program was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

All current upgrades and future improvements are independent implementations
