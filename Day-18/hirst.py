import random
import turtle

color_list = [(229, 216, 0), (163, 19, 67), (229, 181, 0), (173, 35, 95), (246, 60, 31), (72, 184, 0), (243, 66, 0), (251, 123, 72), (175, 132, 177), (3, 108, 154), (161, 206, 213), (183, 184, 208), (247, 197, 23), (167, 170, 197), (69, 24, 67), (235, 64, 97), (179, 209, 221), (166, 9, 1), (107, 93, 0), (13, 48, 77), (56, 147, 1), (42, 98, 1), (118, 8, 0), (163, 205, 204), (60, 51, 96), (114, 119, 160), (29, 76, 0), (38, 154, 186), (6, 84, 111), (156, 199, 198)]
print(len(color_list))

from turtle import Turtle,Screen

tim = Turtle()
turtle.colormode(255)
sc = Screen()

tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100


for i in range(1,no_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if i%10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


sc.exitonclick()

