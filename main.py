from turtle import Screen
from paddle import Paddle
from ball import Ball
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

screen.onkey(key="Up", fun=l_paddle.move_up)
screen.onkey(key="Down", fun=l_paddle.move_down)
screen.onkey(key="w", fun=r_paddle.move_up)
screen.onkey(key="s", fun=r_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
screen.exitonclick()
