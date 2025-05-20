from turtle import Turtle,Screen

tim = Turtle()
sc = Screen()

def frwd():
    tim.forward(20)

def bck():
    tim.backward(20)

def cc():
    tim.left(20)

def clk():
    tim.right(20)

def clr():
    tim.clear()
    tim.home()
    tim.pendown()


sc.onkey(frwd,"W")
sc.listen()
sc.onkey(bck,"S")
sc.onkey(cc,"A")
sc.onkey(clk,"D")
sc.onkey(clr,"C")

sc.exitonclick()