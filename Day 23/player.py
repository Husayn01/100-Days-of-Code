from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.left(90)
        self.move_distance = 10
        self.reset_pos()

    def move(self):
        self.forward(self.move_distance)
    
    def reset_pos(self):
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
    

