import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the speed to the fastest

# Function to draw a Phyllotaxis spiral
def draw_phyllotaxis(num_leaves):
    for i in range(num_leaves):
        t.forward(i * 2)  # Move forward by a distance that increases with each leaf
        t.left(137.5)  # Turn left by the golden angle

# Draw the Phyllotaxis spiral
draw_phyllotaxis(500)

# Keep the window open until it is clicked.
screen.exitonclick()