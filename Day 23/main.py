import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.onkey(player.move, "w")
    screen.update()
    cars.create_car()
    cars.move()

    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() >= 280:
        player.back_to_start()
        cars.level_up()
        scoreboard.update()

scoreboard.game_over()
screen.exitonclick()
