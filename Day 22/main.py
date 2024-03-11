from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
scoreboard = Scoreboard()
ball = Ball()
game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle1) < 60 and ball.xcor() > 320) or (ball.distance(paddle2) < 60 and ball.xcor() < -320):
        ball.bounce_x()
    if ball.distance(paddle1) > 60 and ball.xcor() > 320:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.distance(paddle2) > 60 and ball.xcor() < -320:
        ball.reset_pos()
        scoreboard.r_point()
screen.exitonclick()
