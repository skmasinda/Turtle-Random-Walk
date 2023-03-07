from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")


""" This is a program that draws various shapes with various colors"""

"""In this next exercise tim the turtle will create a random walk """

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

t.colormode(255)
angles = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(10)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(angles))



screen = Screen()
screen.exitonclick()
