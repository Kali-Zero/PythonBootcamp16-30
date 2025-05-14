import random
from turtle import Turtle, Screen, colormode, color

#https://docs.python.org/3/library/turtle.html

#Aliasing - import something and basically renaming it
#import random as rng

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

#Make a square!=====================================
# i = 0
# while i <= 3:
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
#     i += 1
# timmy_the_turtle.forward(100)

#Make a square, but better.==========================
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

#Make a dotted line=================================
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#Draw shapes... with random colors!==================
# i = 3 #number of sides
# while i <= 10:
#     for _ in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360 / i)
#     i+= 1
#     timmy_the_turtle.color(random.random(), random.random(), random.random())

#Random Walk=========================================
# timmy_the_turtle.speed(0)
# timmy_the_turtle.pensize(15)
# for _ in range(200):
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice([0, 90, 180, 270]))
#     timmy_the_turtle.color(random.random(), random.random(), random.random())

#Spirograph===========================================
timmy_the_turtle.speed(0)
for _ in range(100):
    timmy_the_turtle.circle(100) #Size of circle
    timmy_the_turtle.color(random.random(), random.random(), random.random())
    timmy_the_turtle.right(3.6) #360 / 100 = 3.6 (for 100 circles)

#====Put all this last
screen = Screen()
#Keeps the window from disappearing until we click on it
screen.exitonclick()