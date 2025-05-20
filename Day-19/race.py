import random
from turtle import Turtle,Screen


is_race_on = False

sc = Screen()

sc.setup(width=500,height=400)
user_input = sc.textinput(title="Make your bet ",prompt="Which is your turtle ?")
colors = ["red","blue","green","yellow","orange","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtle = []


for i in range(6):
    new_tutle = Turtle(shape= "turtle")
    new_tutle.penup()
    new_tutle.color(colors[i])
    new_tutle.goto(-230,y_position[i])
    all_turtle.append(new_tutle)


if user_input:
    is_race_on = True

while is_race_on:

    for turt in all_turtle:
        if turt.xcor() >230:
            is_race_on = False
            winning_color = turt.pencolor()

            if winning_color == user_input:
                print("you won")
            else:
                print(f"you lose{winning_color} is first")
        rand_dist = random.randint(0,10)
        turt.forward(rand_dist)


sc.exitonclick()