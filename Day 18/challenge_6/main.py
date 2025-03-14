import turtle
from turtle import Turtle, Screen
import random
import colorgram

turtle.colormode(255)

# Extract colors from image
colors = colorgram.extract('C:/Users/Hussaini/Desktop/100-Days-of-Code/Day 18/challenge_6/image.jpg', 10)
color_list = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors]

# Turtle setup
t = Turtle()
t.speed("fastest")  # Speed up drawing
t.hideturtle()  # Hide turtle for cleaner output
t.penup()  # Avoid drawing connecting lines

# Grid parameters
dot_size = 20
spacing = 50  # Space between dots
rows = 10
cols = 10
start_x = - (cols // 2) * spacing  # Centering x-position
start_y = - (rows // 2) * spacing  # Centering y-position

# Drawing dots
for i in range(rows):
    for j in range(cols):
        t.goto(start_x + j * spacing, start_y + i * spacing)
        t.dot(dot_size, random.choice(color_list))

# Screen exit on click
screen = Screen()
screen.exitonclick()
