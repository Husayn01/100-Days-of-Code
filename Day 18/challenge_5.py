from turtle import Turtle, Screen
    
t = Turtle()
t.speed("fastest") 
r = 70

for i in range (36):
    t.circle(r) 
    t.setheading(t.heading() + 10)
screen = Screen()
screen.exitonclick()