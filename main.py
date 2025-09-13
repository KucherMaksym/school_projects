import random
import tkinter as tk
import turtle
import math

def generate_random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

# Generating sides and angles of a triangle
A = random.randint(50, 500)
B = random.randint(50, 500)
angleC = random.randint(30, 150)

# Law of cosines
C = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(angleC)))
# Law of cosines cosA = (B^2 + C^2 - A^2) / (2*B*C)
cosA = (B*B + C*C - A*A) / (2 * B * C)
cosA = max(-1.0, min(1.0, cosA)) # Error protection
angleA = math.degrees(math.acos(cosA))

# No need to use the law of sines here
angleB = 180 - angleC - angleA

'''
    There are 2 different libs to draw triangle: tkinter and turtle.
    Turtle - supports "movement" of brush 
    Tkinter - supports drawing by coordinates
    Here I use 2 different approaches to draw triangle (1 - for tkinter, 2 - for turtle)
'''

# Turtle

print(f" A = {A}, B = {B}, C = {C}")
print(f" angleC = {angleC}, angleBC = {angleA}, angleCA = {angleB}")

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Random Triangle")
screen.setup(800, 600)

t = turtle.Turtle()
t.pencolor(generate_random_rgb_color())
t.width(random.randint(1, 10))

t.speed(0)
t.right(random.randint(0, 359))
t.forward(A)
t.left(180 - angleC) # 180 - angle = outer angle
t.forward(B)
t.left(180 - angleA)
t.forward(C)
t.left(180 - angleB)
t.hideturtle()

screen.mainloop()