from turtle import Turtle,Screen
import random

tim = Turtle()
sc = Screen()

colors = ["light coral","green yellow","cadet blue","sienna","dark violet","navy","dark magenta","crimson","dark turquoise","yellow"]
for i in range(3,11):
    tim.color(random.choice(colors))
    angle = 360 // i
    for j in range(i):
        tim.right(angle)
        tim.forward(50)
sc.exitonclick()