import turtle
import random
from turtle import Turtle, Screen
screen = Screen()

#The Etch-A-Sketch==============================================
# timmy_the_turtle = Turtle()
#
# def move_forward():
#     timmy_the_turtle.forward(10)
# def move_backward():
#     timmy_the_turtle.backward(10)
# def turn_left():
#     timmy_the_turtle.left(10)
# def turn_right():
#     timmy_the_turtle.right(10)
# def clear_screen():
#     timmy_the_turtle.clear()
#     timmy_the_turtle.penup()
#     timmy_the_turtle.home()
#     timmy_the_turtle.pendown()
#
# screen.listen()
# #No parenthesis for functions called as an argument!
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_screen, "c")

#The Turtle Race=================================================
is_race_on = False
screen.setup(width=600, height=600)
user_bet = turtle.textinput(title="Make A Bet!", prompt="Which color are you betting on? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

#Creating multiple objects from the same class
for turtle_index in range(0, 6):
    race_turtle = Turtle(shape="turtle")
    race_turtle.color(colors[turtle_index])
    race_turtle.turtlesize(2)
    race_turtle.penup()
    race_turtle.goto(x=-250, y=y_positions[turtle_index])
    all_turtles.append(race_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! The {winning_color} turtle is the winner!")
            else:
                print(f"You Lose. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        #Just for a little extra color
        turtle.pendown()
        turtle.pensize(5)
        turtle.forward(random_distance)

screen.exitonclick()