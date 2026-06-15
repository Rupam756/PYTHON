import random
import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white") # Screen background color

t = turtle.Turtle() 
t.speed(3)  # Set a moderate speed so you can see it drawing

# Function to draw a square (Base of the hut)
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.left(90)  

# Function to draw a triangle (Roof of the hut)
def draw_triangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

# Function to draw a hut with random properties
def draw_hut():
    # 1. Random size choose kora (between 80 to 150 pixels)
    size = random.randint(80, 150)
    
    # 2. Random colors select kora
    colors = ["brown", "blue", "red", "darkgreen", "purple", "orange", "magenta"]
    base_color = random.choice(colors)
    roof_color = random.choice(colors)
    
    # Draw the base of the hut
    t.color(base_color)
    t.begin_fill()
    draw_square(size)
    t.end_fill()
    
    # Move the turtle to the top left of the square to start the roof
    t.penup()
    t.goto(0, size)
    t.pendown()
    
    # Draw the roof of the hut
    t.color(roof_color)
    t.begin_fill()
    draw_triangle(size)  
    t.end_fill()

# Main function to execute the drawing
def main():
    draw_hut()
    t.hideturtle() # Turtle icon ta hide korar jonno
    screen.exitonclick()  # Screen ta stay korbe, click korle close hobe

if __name__ == "__main__":
    main()