import turtle
from turtle import Turtle,Screen
import random

tim = Turtle()
sc = Screen()
turtle.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r,g,b

i = 0

## 360/gap(here 10)
while i< 361:
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() +10)
    i+=1















sc.exitonclick()