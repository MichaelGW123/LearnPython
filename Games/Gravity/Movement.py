#Michael Williamson
#Practicing programming Gravity (basic movement)
#7/25/2020

import turtle

# Window
screen = turtle.Screen()
screen.title("Gravity Test")
screen.setup(width=800, height= 600)
screen.bgcolor("white")
screen.tracer(0)

# Block
block = turtle.Turtle()
block.speed(0)
block.penup()
block.color("pink")
block.shape("square")
block.goto(0,0)

# Movement functions
def moveUp():
    if block.ycor() < 290:
        block.sety(block.ycor() + 10)


def moveDown():
    if block.ycor() > -280:
        block.sety(block.ycor() - 10)


def moveLeft():
    if block.xcor() > -390:
        block.setx(block.xcor() - 10)


def moveRight():
    if block.xcor() < 380:
        block.setx(block.xcor() + 10)


# Movement capture
screen.listen()
screen.onkeypress(moveUp, "w")
screen.onkeypress(moveDown, "s")
screen.onkeypress(moveLeft, "a")
screen.onkeypress(moveRight, "d")

while True:
    screen.update()
