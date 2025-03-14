from turtle import Turtle, Screen

timmy = Turtle()

# for i in range(10):
#     timmy.forward(10)
#     timmy.color("white")
#     timmy.forward(10)
#     timmy.color("black")

for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()