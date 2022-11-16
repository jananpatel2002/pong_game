from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("White")
        self.goto(x, y)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
