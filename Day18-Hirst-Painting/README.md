# Day 18 - Hirst Painting
Author: Vindhya Hasini

## Description
This program is a Python implementation of the Hirst-style dot painting.

The project uses Python's turtle graphics module to recreate the iconic style of the famous painter Damien Hirst by
drawing a colorful grid of randomly selected dots. The color palette is extracted from an image using the colorgram.py
package, allowing the artwork to closely resemble the actual painting.

## Files in this directory
| File Name | Description                                                     | Status      |
|-----------|-----------------------------------------------------------------|-------------|
| main.py   | Contains the code for the Hirst Painting project                | ✅ Completed |
| image.jpg | Contains an image of the actual painting to extract colors from | ✅ Completed |


## Concepts Learned
* Working with the Python turtle graphics module
* Creating graphical applications
* RGB color representation
* Setting turtle color mode
* Using colorgram.py to extract any number of colors from any image with file extension .jpg
* Python tuples
* Random color selection using the random module
* Positioning and moving the turtle around the screen

## Features in the Original Version (main.py)
* Extracts a custom color palette from the uploaded image (image.jpg)
* Stores colors as RGB tuples
* Draws a 10x10 grid of colorful dots
* Randomly selects a color for each dot
* Uses functions to separate responsibilities and logic
* Produces a different artwork on every run

## Future Improvements
* Allow users to customize the number of rows and columns
* Allow users to customize the spacing between the dots
* Allow users to specify the dot size
* Generate different painting sizes automatically
* Save the artwork as an image

## Key Takeaways

This project introduced me to graphical programming using Python and showed how code can be used to generate artwork.
Some of my biggest takeaways are:
* There are often multiple valid ways to solve the same problem.
I initially created each "dot" by increasing the pen size and moving the Turtle a single step before later discovering 
that Turtle provides a dedicated dot() method.
* Breaking the program into smaller functions made the code easier to read and maintain.
* External libraries can greatly simplify tasks such as extracting colors from an image.
* Combining randomness with graphics can produce unique and visually appealing results.

## Challenges Faced
When working with new modules, it is very important to study the methods and functions in that module using its documentation.
This was quite challenging as I had to learn about the turtle methods before writing any code. However, it simplified my 
coding process significantly.

Another big challenge was figuring out how to use the colorgram.py module to extract RGB values for colors in a chosen 
image. 

Another challenge was deciding how to create the dots for the painting. Before seeing the course solution, 
I experimented with using a large pen size and moving the Turtle a single step to simulate a dot. 
Although I later learned about Turtle's built-in dot() method, solving the problem independently helped strengthen my 
problem-solving skills and reinforced that there are often multiple ways to reach the same result.

## Note
This program was completed as a part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp

The code for the process of extraction of colors from the image is commented out because of using the extracted color list
from a previous run. 

I choose to keep the code containing the logic I figured out myself, before watching the solution of the instructor.

All future improvements will be independent implementations.
