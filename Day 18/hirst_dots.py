import random
from turtle import Turtle, Screen, colormode, color
#import colorgram
#https://pypi.org/project/colorgram.py/
#The color extractor!====================================================
# rgb_colors = []
# colors = colorgram.extract('hirstLike.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

#Result from code above====================================================
#Don't forget to remove colors that are too hard to see, like white, etc...
color_list = [(7, 17, 14), (230, 151, 89), (24, 113, 162), (22, 11, 7), (38, 13, 23), (237, 219, 84),
              (109, 171, 206), (11, 181, 220), (211, 76, 106), (147, 78, 54), (151, 63, 89), (30, 133, 92),
              (154, 19, 38), (213, 127, 158), (227, 79, 56), (38, 178, 122), (244, 218, 167), (251, 163, 143),
              (115, 194, 128), (161, 182, 39), (5, 106, 84), (111, 225, 241), (7, 90, 106), (242, 209, 229),
              (110, 113, 175), (192, 221, 240), (240, 160, 186), (40, 58, 103), (237, 213, 6)]

#Paint the canvas in colored circles=======================================
turtle_cursor = Turtle()
turtle_cursor.hideturtle()
colormode(255)
turtle_cursor.speed(0)
turtle_cursor.penup()
turtle_cursor.goto(-250,-250)
i = 1
while i <= 10:
    for _ in range(10):
        turtle_cursor.color(random.choice(color_list))
        turtle_cursor.dot(20)
        turtle_cursor.forward(50)
    turtle_cursor.goto(-250, -250)
    turtle_cursor.left(90)
    turtle_cursor.forward(50 * i)
    turtle_cursor.right(90)
    i += 1

screen = Screen()
screen.exitonclick()