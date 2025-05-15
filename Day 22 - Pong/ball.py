from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        #Takes the current x-coordinate, and adds 10
        new_x = self.xcor() + self.x_move
        #Takes the current y-coordinate, and adds 10
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        #Takes the y_move (10) and reverses it (-10) Making it go from UP to DOWN (or vice versa)
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
