from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.speed("slowest")
        self.penup()
        self.direction = 'up'

    # Bouncing Logic for walls is written
    def move(self):
        if self.direction == 'down' and self.ycor() > -280:
            self.goto(self.xcor() + 10, self.ycor() - 10)
        elif not self.ycor() > -280 and self.direction == 'down':
            self.direction = 'up'
            self.goto(self.xcor() + 10, self.ycor() + 10)
        elif self.ycor() < 280 and self.direction == 'up':
            self.goto(self.xcor() + 10, self.ycor() + 10)
        elif not self.ycor() < 280 and self.direction == 'up':
            self.direction = 'down'
            self.goto(self.xcor() + 10, self.ycor() - 10)

    def change_direction(self):
        pass
