from turtle import Turtle

P1_PADDLE_START = (350, 0)


class Paddle(Turtle):
    def __init__(self, paddle_start):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.color('white')
        self.penup()
        self.goto(paddle_start)

    # def create_paddle(self):
    #     paddle = Turtle('square')
    #     paddle.turtlesize(stretch_wid=1, stretch_len=5)
    #     paddle.setheading(90)
    #     paddle.color('white')
    #     paddle.penup()
    #     paddle.goto(P1_PADDLE_START)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
