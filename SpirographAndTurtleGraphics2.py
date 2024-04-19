import turtle
import math
import random

# Function to draw the Spirograph pattern
def draw_spirograph(t, R, r, d, l):
    # Calculate the number of iterations needed to complete the spirograph
    num_loops = abs(R // math.gcd(R, r))
    num_iters = l * num_loops
    step_angle = 360 / num_loops

    for _ in range(num_iters):
        t.pencolor(random.choice(colors))  # Change color
        t.circle(r, step_angle)  # Move in the small circle
        t.left(step_angle)
        t.forward(d)

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the speed to the fastest
t.hideturtle()  # Hide the turtle cursor

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Main loop
draw_spirograph(t, 160, 80, 50, 10)  # Example parameters for R, r, d, and l (loop factor)

# Keep the window open until it is clicked.
screen.exitonclick()