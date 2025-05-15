from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorekeeper import Scorekeeper
import time

#Create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#Create the paddle (coordinates are starting positions)
scorekeeper = Scorekeeper()

r_paddle = Paddle((350,0))
#Create another paddle
l_paddle = Paddle((-350,0))
#Create the ball and make it move
ball = Ball((0,0))
ball.move_ball()

screen.listen()
#Move the right paddle
#Remember, NO PARENTHESIS AFTER FUNCTION NAMES WHEN CALLED FROM WITHIN ANOTHER FUNCTION!!!
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down,"Down")
#Move the left paddle
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down,"s")

game_is_on = True
while game_is_on:
    #time.sleep(ball.ball_speed) #Will make ball go faster when hit by paddle
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    #Detect collision with top or bottom walls.
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_bounce()

    #Detect collision with paddles,
    if (ball.distance(r_paddle) < 45 and ball.xcor() < 330 or
            ball.distance(l_paddle) < 45 and ball.xcor() > -330):
        ball.x_bounce()

    #Detect collision with right wall.
    if ball.xcor() > 380:
        ball.reset_position()
        ball.ball_speed = 0.1
        scorekeeper.l_point()

    #Detect collision with left wall.
    if ball.xcor() < -380:
        ball.reset_position()
        scorekeeper.r_point()

screen.exitonclick()