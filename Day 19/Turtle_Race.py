from turtle import Turtle, Screen
import random
import tkinter.simpledialog

def up():
    turtle.setheading(90)
    turtle.forward(10)


def down():
    turtle.setheading(270)
    turtle.forward(10)


def right():
    turtle.setheading(0)
    turtle.forward(10)


def left():
    turtle.setheading(180)
    turtle.forward(10)


def clock():
    turtle.right(10)
    turtle.forward(10)


def counter():
    turtle.left(10)
    turtle.forward(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen = Screen()
screen.setup(500, 400)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtles = []


for c in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[c])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[c])
    turtles.append(new_turtle)

race_start = False

user_bet = screen.textinput("Make your bet!  ", "Which turtle will win the race? Enter a color: ")


if user_bet:
    race_start = True

while race_start:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_start = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")
        distance = random.randint(0, 10)
        turtle.forward(distance)


# turtle = Turtle(shape="turtle")
#
# screen.listen()
# screen.onkey(up, "w")
# screen.onkey(down, "s")
# screen.onkey(right, "d")
# screen.onkey(left, "a")
# screen.onkey(clock, "e")
# screen.onkey(counter, "q")
# screen.onkey(clear, "c")
screen.exitonclick()
