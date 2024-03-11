from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(x,y)
        self.color("white")
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
