from turtle import Turtle, Screen
import random

timmy = Turtle()
list = [3, 4, 5, 6, 7, 8, 9, 10]
colors = ['red', "blue", "green", "yellow", "purple", "pink", "black", "cyan"]
for item in list:
    def draw():
        timmy.color(random.choice(colors))
        for _ in range(item):
            timmy.forward(100)
            timmy.right(360 / item)
    draw()

screen = Screen()
screen.exitonclick()