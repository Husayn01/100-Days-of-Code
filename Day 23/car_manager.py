from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    def __init__(self):
        self.all_cars = []  # Store multiple cars
        self.move_speed = 5  # Initial car speed

    def create_car(self):
        """Creates a new car at a random position."""
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(280, random.randint(-250, 250))  # Start from the right
        self.all_cars.append(new_car)

    def move(self):
        """Moves all cars in the list."""
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increase_speed(self):
        """Increases car speed when the turtle reaches the finish line."""
        self.move_speed += 3
