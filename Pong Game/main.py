import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

leftPaddle = Paddle((-380, 0))
rightPaddle = Paddle((370, 0))
ball = Ball()

screen.listen()
screen.onkeypress(rightPaddle.go_up, "Up")
screen.onkeypress(rightPaddle.go_down, "Down")
screen.onkeypress(leftPaddle.go_up, "w")
screen.onkeypress(leftPaddle.go_down, "s")

game = True
while game:
    time.sleep(0.2)
    screen.update()
    ball.move()

    # Detecting Collisions
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # Detecting Collision with Paddles
    if ball.distance(rightPaddle)<50 and ball.xcor()>320 or ball.distance(leftPaddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

screen.exitonclick()