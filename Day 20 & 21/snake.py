from turtle import Turtle, Screen
import time
SPEED = 20
class Snake():
    def __init__(self):
        self.segments = []
        for i in range(0, 3):
            tmp = Turtle()
            tmp.shape("square")
            tmp.color("white")
            tmp.penup()
            pos = i * (-20)
            tmp.setpos(pos, 0)
            self.segments.append(tmp)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x, new_y = self.segments[seg - 1].xcor(), self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(SPEED)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def extend(self):
        tmp = Turtle()
        tmp.shape("square")
        tmp.color("white")
        tmp.penup()
        tmp.goto(self.segments[-1].position())
        self.segments.append(tmp)

