from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score =0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
       

    def update_score(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"{self.l_score}",align="center",font=("Arial",30,"normal"))
        self.goto(100,250)
        self.write(f"{self.r_score}",align="center",font=("Arial",30,"normal"))
    
    def left_update(self):
        self.l_score+=1
        self.update_score()
    
    def right_update(self):
        self.r_score+=1
        self.update_score()

