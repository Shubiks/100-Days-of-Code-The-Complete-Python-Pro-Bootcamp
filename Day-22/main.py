from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

myscreen = Screen()
myscreen.bgcolor("black")
myscreen.setup(height=600,width=800)
myscreen.title("pong")
myscreen.tracer(0)

right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()


myscreen.listen()
myscreen.onkey(right_paddle.up,"Up")
myscreen.onkey(right_paddle.down,"Down")
myscreen.onkey(left_paddle.up,"w")
myscreen.onkey(left_paddle.down,"s")

game_is_on = True
x = 60
y = 60

while game_is_on:
    time.sleep(0.1)

    myscreen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce()


    if ball.distance(right_paddle)<50 and ball.xcor() >320 or ball.distance(left_paddle)<50 and ball.xcor() <-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_pos()
        scoreboard.left_update()

    if ball.xcor()<-380:
        ball.reset_pos()
        scoreboard.right_update()

myscreen.exitonclick()