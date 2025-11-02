# Antonio Armwood
# 11/1/2025
# P4LAB1
# Turtle Art

import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(2)
t.shape("turtle")

# Move to a position for initials
t.penup()
t.goto(-150, -150)
t.pendown()

# Draw first "A"
t.left(75)
t.forward(100)
t.right(150)
t.forward(100)
t.backward(50)
t.left(75)
t.backward(25)

# Move to draw second "A"
t.penup()
t.goto(50, -150)
t.setheading(0)
t.pendown()

# Draw second "A"
t.left(75)
t.forward(100)
t.right(150)
t.forward(100)
t.backward(50)
t.left(75)
t.backward(25)
t.penup()
t.goto(200, 200)
t.setheading(0)
t.pendown()

# Finish
turtle.done()
