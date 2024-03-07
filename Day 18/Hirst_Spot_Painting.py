from turtle import Turtle, Screen
import random
import colorgram
# color = colorgram.extract('image.jpg', 30)
# print(color)
# rgb_colors=[]
# for c in color:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]
turtle = Turtle()
screen = Screen()
screen.colormode(255)
# turtle.hideturtle()
turtle.penup()
turtle.left(180)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.speed("fastest")
turtle.setheading(0)
for _ in range(10):
    for _ in range(10):
        turtle.color(random.choice(color_list))
        turtle.dot(20)
        turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)

screen.exitonclick()

