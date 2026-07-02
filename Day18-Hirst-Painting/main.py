import turtle as t
import random
#Extracting colors from the image
# import colorgram
#
# colors = colorgram.extract('image.jpg', 21)
#
# list_of_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     list_of_colors.append((r, g, b))
#
# print(list_of_colors)

extracted_colors = [(231, 206, 85), (218, 229, 219), (254, 218, 226), (224, 150, 89), (215, 224, 230),
                    (120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144), (8, 97, 38),
                    (171, 21, 16), (199, 65, 28), (185, 186, 27), (31, 128, 47), (12, 41, 74), (15, 63, 40),
                    (242, 202, 5), (138, 82, 95), (85, 15, 22)]


vin = t.Turtle()
t.colormode(255)

def paint_one_line():
    vin.pensize(20)
    for rows in range(10):
        vin.color(random.choice(extracted_colors))
        vin.forward(1)
        vin.penup()
        vin.forward(50)
        vin.pendown()


def go_to_next_line():
    vin.penup()
    vin.backward(510)
    vin.left(90)
    vin.forward(50)
    vin.right(90)
    vin.pendown()


start_x = -200
start_y = -200
vin.penup()
vin.goto(start_x, start_y)
vin.pendown()

for columns in range(10):
    paint_one_line()
    go_to_next_line()


screen = t.Screen()
screen.exitonclick()