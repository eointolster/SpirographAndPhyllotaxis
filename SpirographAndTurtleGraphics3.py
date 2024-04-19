import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the speed to the fastest
t.hideturtle()  # Hide the turtle cursor

# Define parameters
R = 200  # Radius of the outer circle
r = 50   # Radius of the inner circle
d = 20   # Distance of the pen from the center of the inner circle
l = 10   # Loop factor

# Function to draw the Spirograph pattern
def draw_spirograph(R, r, d, l):
    t.penup()
    t.goto(0, 0)
    t.pendown()

    for i in range(l * 360):
        t.pencolor("white")  # Change color
        t.circle(r, 1)  # Move in the small circle
        t.left(1)
        t.forward(d)

# Draw the Spirograph pattern
draw_spirograph(R, r, d, l)

# Keep the window open until it is clicked.
screen.exitonclick()