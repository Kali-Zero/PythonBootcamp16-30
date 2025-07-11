from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        #All these functions come from the Turtle class, Inherited with the '(Turtle)' and 'super().__init__()'
        # addons to the current function
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)