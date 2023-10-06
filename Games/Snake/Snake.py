#Michael Williamson
#Snake Game movement practice 
#7/26/2020

import turtle
import time
import random

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

# Snake food
food = turtle.Turtle()
food.shape("square")
food.color("grey")
food.speed(0)
food.penup()
food.goto(0,100)

segments = []

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    
    if head.direction == "right":
        head.setx(head.xcor() + 20)


# Keyboard Bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# Main game loop
while True:
    window.update()

    # Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() >290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for bodypart in segments:
            bodypart.clear() #To clear from screen
            bodypart.ht() #To hide it
            del bodypart #To delete it
        segments.clear()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-14, 14)
        y = random.randint(-14, 14)
        x *= 20
        y *= 20
        # Move the food to a random spot
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order (from tail to head)
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    time.sleep(delay)

window.mainloop()