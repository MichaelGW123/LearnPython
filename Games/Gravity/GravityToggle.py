#Michael Williamson
#Movement practice (Constant)
#7/26/2020

import turtle
import time

delay = 0.1

# Set up screen
window = turtle.Screen()
window.title("Snake")
window.bgcolor("black")
window.setup(width= 600, height= 600)
window.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"
head.gravity = False
head.fallSpeed = 2

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def full_stop():
    head.direction = "stop"

def gravity():
    if head.gravity == True:
        head.gravity = False
        head.fallSpeed = 0
    else:
        head.gravity = True

def move():
    if head.direction == "up" and head.ycor() < 270:
        head.sety(head.ycor() + 20)
    elif head.direction == "down" and head.ycor() > -270:
        head.sety(head.ycor() - 20)
    elif head.direction == "left" and head.xcor() > -270:
        head.setx(head.xcor() - 20)
    elif head.direction == "right" and head.xcor() < 270:
        head.setx(head.xcor() + 20)

    if head.gravity == True and (head.ycor() - head.fallSpeed) > -270:
        head.sety(head.ycor() - head.fallSpeed)
        head.fallSpeed *= 1.1


# Keyboard Bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(full_stop, "space")
window.onkeypress(gravity, "g")

# Main game loop
while True:
    window.update()

    move()

    time.sleep(delay)

window.mainloop()