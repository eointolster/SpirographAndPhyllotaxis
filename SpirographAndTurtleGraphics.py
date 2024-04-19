import turtle
import math
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the speed to the fastest
t.hideturtle()  # Hide the turtle cursor

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "cyan"]

# Define parameters
R = 200  # Radius of the outer circle
r = 100  # Radius of the inner circle
d = 50   # Distance of the pen from the center of the inner circle

# Function to draw the Spirograph pattern
def draw_spirograph(R, r, d):
    t.penup()
    t.goto(R - r + d, 0)
    t.pendown()

    for i in range(360):
        t.pencolor(random.choice(colors))
        t.pensize(2)  # Increase the pen size for thicker lines
        
        # Calculate the position of the pen
        angle = i * math.pi / 180
        x = (R - r) * math.cos(angle) + d * math.cos((R - r) / r * angle)
        y = (R - r) * math.sin(angle) - d * math.sin((R - r) / r * angle)
        
        t.goto(x, y)

# Animation loop
while True:
    t.clear()
    draw_spirograph(R, r, d)
    R -= 5
    r -= 5
    d += 5

    if R <= 0 or r <= 0:
        R = random.randint(100, 300)  # Randomly select a new value for R
        r = random.randint(50, 200)   # Randomly select a new value for r
        d = random.randint(20, 100)   # Randomly select a new value for d

# Exit the screen on click
screen.exitonclick()