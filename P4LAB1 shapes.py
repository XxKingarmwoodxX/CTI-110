# Antonio Armwood
# 11/1/2025
# P4LAB1
# Turtle Art

import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(2)
t.shape("turtle")

### --- Part A: Draw a square and a triangle (with no overlap) ---

# Draw square
t.penup()
t.goto(-200, 100)  # Position for square
t.pendown()
for _ in range(4):
    t.forward(100)
    t.left(90)

# Draw triangle
t.penup()
t.goto(50, 100)  # Position for triangle (with no overlap)
t.setheading(0)
t.pendown()
for _ in range(3):
    t.forward(100)
    t.left(120)



