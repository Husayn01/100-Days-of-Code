import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")

loop = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a new car every sixth loop
    loop += 1
    if loop % 6 == 0:
        car_manager.create_car()

    # Move all cars
    car_manager.move()

    # Detect collision with any car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:  # Adjust collision range
            game_is_on = False
            print("Game Over")

    # Detect when the player reaches the finish line
    if player.ycor() >= 280:
        score.level += 1
        score.update_score()
        player.reset_pos()
        car_manager.increase_speed()  # Increase car speed

screen.exitonclick()
