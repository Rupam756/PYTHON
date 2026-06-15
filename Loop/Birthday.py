'''WRITE A python program to wish someone on their birthday
unique and creative way. You can use any libraries or modules you like to make it more fun and personalized.
'''
import datetime
import random
import turtle
# Function to draw a birthday cake
def draw_cake():
    t = turtle.Turtle()
    t.speed(1)
    t.color("pink")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()
    
    # Draw candles
    for i in range(5):
        t.penup()
        t.goto(-80 + i*40, 100)
        t.pendown()
        t.color("yellow")
        t.begin_fill()
        for _ in range(4):
            t.forward(10)
            t.left(90)
        t.end_fill()
    t.hideturtle()
# Function to display a birthday message
def display_message(name):
    print(f"Happy Birthday, {name}! Wishing you a day filled with love and joy!")
# Main function to execute the program
def main():
    name = input("Enter the name of the birthday person: ")
    display_message(name)
    draw_cake()     
if __name__ == "__main__":    main()

