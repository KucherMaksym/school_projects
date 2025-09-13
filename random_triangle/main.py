from turtle_drawer import TurtleDrawer
from tkinter_drawer import TkinterDrawer

'''
    There are 2 different libs to draw triangle: tkinter and turtle.
    Turtle - supports "movement" of brush 
    Tkinter - supports drawing by coordinates
    Here I use 2 different approaches to draw triangle (1 - for tkinter, 2 - for turtle)
'''

approach = input("""
What approach to use?

Tkinter - 1    
Turtle - 2
    
(default - 1): """)

if approach == "2":
    drawer = TurtleDrawer()
    drawer.draw_turtle_triangle()
else:
    drawer = TkinterDrawer()
    drawer.draw_tkinter_triangle()