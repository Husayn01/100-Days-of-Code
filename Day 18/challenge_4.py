from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(5)
def forward():
    timmy.forward(20)

def backward():
    timmy.backward(20)

def right():
    timmy.right(90)

def left():
    timmy.left(90)
func_dir = [forward, backward,]
func_angle = [right, left]
colors = ['red', "blue", "green", "yellow", "purple", "pink", "black", "cyan"]

for i in range(500):
    random.choice(colors)
    random.choice(func_dir)()
    random.choice(func_angle)()

screen = Screen()
screen.exitonclick()