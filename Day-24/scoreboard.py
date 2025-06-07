from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            d = data.read()
            self.high_score = int(d)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scroreboard()

    def update_scroreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("center",16,"normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scroreboard()
        


    
    def increase_score(self):
        self.score+=1
        self.update_scroreboard()