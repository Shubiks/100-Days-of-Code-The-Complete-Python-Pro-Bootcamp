import turtle
from turtle import Turtle,Screen

import random

turtle.colormode(255)

jim = Turtle()
my_screen = Screen()
jim.pensize(10)
jim.speed("fast")

directions = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b
i =0
while i < 100:
    jim.color(random_color())
    jim.setheading(random.choice(directions))
    jim.forward(25)

    i+=1

my_screen.exitonclick()
