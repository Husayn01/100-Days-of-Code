from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.level = 1
      self.color("black")
      self.hideturtle() 
      self.penup()
      self.update_score()

    def update_score(self):
       self.clear()
       self.goto(-220,270)
       self.write(f"Level: {self.level}", align= "center", font= FONT)

