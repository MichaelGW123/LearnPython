#Michael Williamson
#Practicing programming Gravity
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

# Floor
floor = turtle.Turtle()
floor.speed(0)
floor.penup()
floor.shape("square")
floor.color("black")
floor.shapesize(stretch_len=30,stretch_wid=1)
floor.goto(0,-250)

# Gravity
gravity = 0.002

# Fall Speed
fallSpeed = 0

# Jump
jump = 2

# and (block.xcor() - 10 > floor.xcor() - 100)
def onGround():
    if ((block.ycor() - 10) == (floor.ycor() + 10)) and (block.xcor() + 10 < floor.xcor() + 100):
        return True
    else:
        return False


def willBeOnGround(fall):
    if (block.ycor() - fall) < (floor.ycor() + 10) and (block.xcor() + 10 < floor.xcor() + 100):
        block.sety(floor.ycor()+20)
        return True
    else:
        return False


def blockMoveLeft():
    block.setx(block.xcor() - 10)


def blockMoveRight():
    block.setx(block.xcor() + 10)


def blockJump():
    pass

# Keyboard Listening
screen.listen()
screen.onkeypress(blockMoveLeft, "a")
screen.onkeypress(blockMoveRight, "d")
screen.onkeypress(blockJump, "w")


while True:
    screen.update()

    if onGround != True:
        fallSpeed += gravity
        block.sety(block.ycor() - fallSpeed)
        if willBeOnGround(fallSpeed) == True:
            fallSpeed = 0
            onGround = True
