from turtle import Turtle,Screen

timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.color()

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# timmy.pencolor("pink")
# timmy.forward(20)
# timmy.penup()
# timmy.forward(20)
# if not timmy.isdown():
#     timmy.pendown()
#     timmy.forward(20)

for i in range(30):
    timmy.pendown()
    timmy.forward(20)
    timmy.penup()
    timmy.forward(20)
    # if not timmy.isdown():
    #     timmy.pendown()
    #     timmy.forward(20)
    #     timmy.penup()

# timmy.backward(50)
my_screen.exitonclick()
