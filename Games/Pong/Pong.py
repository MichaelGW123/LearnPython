#Michael Williamson
#Pong Game practice
#7/24/2020

import turtle

# Create Screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Score
score_left = 0
score_right = 0

# Left paddle
paddleLeft = turtle.Turtle()
paddleLeft.speed(0)
paddleLeft.shape("square")
paddleLeft.color("white")
paddleLeft.shapesize(stretch_wid=5, stretch_len=1)
paddleLeft.penup()
paddleLeft.goto(-350,0)

# Right paddle
paddleRight = turtle.Turtle()
paddleRight.speed(0)
paddleRight.shape("square")
paddleRight.color("white")
paddleRight.shapesize(stretch_wid=5, stretch_len=1)
paddleRight.penup()
paddleRight.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = -0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Movement Functions
def paddleLeftUp():
    y = paddleLeft.ycor()
    if y < 260:
        y += 20
    paddleLeft.sety(y)


def paddleLeftDown():
    y = paddleLeft.ycor()
    if y > -260:
        y -= 20
    paddleLeft.sety(y)


def paddleRightUp():
    y = paddleRight.ycor()
    if y < 260:
        y += 20
    paddleRight.sety(y)


def paddleRightDown():
    y = paddleRight.ycor()
    if y > -260:
        y -= 20
    paddleRight.sety(y)


# Keyboard binding
screen.listen()
screen.onkeypress(paddleLeftUp, "w")
screen.onkeypress(paddleLeftDown, "s")
screen.onkeypress(paddleRightUp, "i")
screen.onkeypress(paddleRightDown, "k")

while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))


    # Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleRight.ycor() + 40 and ball.ycor() > paddleRight.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleLeft.ycor() + 40 and ball.ycor() > paddleLeft.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
