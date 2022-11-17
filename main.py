from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.listen()

screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):

        ball.change_direction()
        ball.move()
        print(ball.move_speed)

    if ball.xcor() >= 400:
        ball.reset_ball()
        scoreboard.update_left()
        scoreboard.update_scoreboard()
        l_paddle.reset_paddle()
        r_paddle.reset_paddle()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.update_right()
        scoreboard.update_scoreboard()
        l_paddle.reset_paddle()
        r_paddle.reset_paddle()
screen.exitonclick()
