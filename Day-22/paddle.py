from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid= 5,stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x_cor, y_cor)


    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)