from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 260: #Keeps paddles on the screen
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - 20)
