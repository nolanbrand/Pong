from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PADDLE_START = (350, 0)
LEFT_PADDLE_START = (-350, 0)

screen = Screen()
screen.title('Pong')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(RIGHT_PADDLE_START)
l_paddle = Paddle(LEFT_PADDLE_START)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.up, key='Up')
screen.onkey(fun=r_paddle.down, key='Down')
screen.onkey(fun=l_paddle.up, key='w')
screen.onkey(fun=l_paddle.down, key='s')

game_on = True
top_wall_contact = False

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    scoreboard.update_scoreboard()

    #Detect collision with wall
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect if ball misses right paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.r_point()
        ball_speed = 0.1
    # Detect if ball misses left paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.l_point()
        ball_speed = 0.1

screen.exitonclick()
