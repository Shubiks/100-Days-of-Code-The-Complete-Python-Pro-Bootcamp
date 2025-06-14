import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turt = Player()
screen.onkey(turt.move_forward,"Up")

cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(turt) <20:
            game_is_on = False
            scoreboard.game_over()

    if turt.is_finish_line():
        turt.goto_start()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()