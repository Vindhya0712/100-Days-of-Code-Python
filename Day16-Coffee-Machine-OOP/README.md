# Day 16 - PyCoffee: Coffee Machine Project (OOP Version)
Author: Vindhya Hasini


## Description
This is the OOP implementation of the Coffee Machine Project completed on Day 15.

Instead of implementing everything from scratch, this project focuses on understanding and integrating pre-written Python 
classes into a fully functional application. The goal was to build a coffee machine by interacting with existing modules 
while improving the user experience with additional features and validations.


## Files in this directory
| File Name        | Description                                                                                                                                                              | Status      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| main.py          | Contains the code for the OOP implementation of the Coffee Machine Project                                                                                               | ✅ Completed |
| menu.py          | Contains the Menu and MenuItem classes that store the available drinks, their ingredients, and prices, while providing methods to retrieve menu items.                   | ✅ Completed |
| coffee_maker.py  | Contains the CoffeeMaker class responsible for tracking available resources, checking ingredient availability, preparing drinks, and generating resource reports         | ✅ Completed |
| money_machine.py | Contains the MoneyMachine class responsible for processing coin payments, validating transactions, calculating change, tracking profits, and generating earnings reports | ✅ Completed |

Note: The class definition files (menu.py, coffee_maker.py, money_machine.py) were provided as part of the course to help
students focus on understanding Object-Oriented-Programming by interacting with existing classes. 
The application logic, program flow, user interaction, validation and interface enhancement is handled by main.py

## Concepts Learned
* Object-Oriented-Programming (OOP)
* Working with existing classes
* Importing custom modules and packages
* Creating and using objects 
* Calling methods from different classes
* Understanding class interactions
* Working with third party libraries (PrettyTable)
* Modular programming
* Input validation
* Refactoring code into smaller functions


## Features in my version (main.py)
* Purchase espresso, latte or a cappuccino
* Coin-operated payment system with automatic change calculation
* Automatic resource management
* Generate reports showing remaining resources and money earned, using PrettyTable
* Reject orders if resources are insufficient
* Turn off the machine using the 'off' command
* Built using OOP concepts by integrating multiple interacting classes
* Monetary values formatted upto 2 decimal places
* Accepts user inputs regardless of accidental leading/trailing spaces


## Future Improvements
* Persistent machine state
* Admin mode to refill ingredients
* Add new beverages/seasonal drinks
* Display transaction history
* Hand out customer receipt
* Allow ordering multiple drinks in one order
* Display a warning message when any resources are depleted
* Daily Sales Report


## Key Takeaways
* Instead of writing every class myself, I learned how to understand existing code, read documentation, create objects, 
and make multiple classes work together to build a complete application.
* Plan the program flow before writing the code
* Read documentation carefully before looking at implementation ideas
* OOP is about getting methods and objects on different classes to work together
* Small improvements to user experience—such as formatted reports, cleaner output and clear messages—can make a terminal application feel much more polished.
* Debugging often comes down to paying attention to tiny details, such as formatting specifiers or understanding which 
object is responsible for a particular task.


## Challenges Faced
* Understanding how multiple pre-written classes work, and can be integrated into our projects
* Planning the overall flow of the project before writing any code
* Reading and understanding the documentation clearly instead of immediately reading the source code
* Determining which class was responsible for which task
* Integrating different classes while keeping the OOP design intact
* Identifying small formatting issues such as floating point display (:.2f) while improving UX


## Note
This project was completed as a part of Dr. Angela Yu's 100 days of Code: The Python Pro Bootcamp

All future improvements will be independent implementations