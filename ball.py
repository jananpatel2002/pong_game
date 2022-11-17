from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.speed("fastest")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Bouncing Logic for walls is written
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1  # Changes the direction of the bounce instead of up, it goes down etc.

    def change_direction(self):
        self.x_move *= -1
        self.move_speed *=.9

    def reset_ball(self):
        self.goto(0, 0)
        self.change_direction()
        self.move_speed = 0.1

    def change_speed(self):

        if self.x_move > 0:
            self.x_move += 5
        else:
            self.x_move -= 5
        if self.y_move > 0:
            self.y_move += 5
        else:
            self.y_move -= 5
