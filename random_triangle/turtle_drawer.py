import turtle
import random
from triangle_utils import TriangleUtils
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TurtleDrawer:
    def __init__(self):
        self.triangle = TriangleUtils()
        self.screen = None
        self.instruction_turtle = None
        self.debug = False

    def draw_instructions(self):
        if self.instruction_turtle is None:
            self.instruction_turtle = turtle.Turtle()
            self.instruction_turtle.hideturtle()
            self.instruction_turtle.speed(0)
            self.instruction_turtle.penup()

        # Position for instructions (top-left corner)
        self.instruction_turtle.goto(-380, 300)
        self.instruction_turtle.color("black")
        self.instruction_turtle.write(
            "Left mouse button - new triangle | Right mouse click - clear and draw a new triangle",
            font=("Arial", 12, "normal")
        )

    def draw_triangle(self):
        A, B, C, angleA, angleB, angleC = self.triangle.generate_random_triangle()

        if self.debug:
            logging.info("Drawing new triangle:")
            logging.info(f" A = {A}, B = {B}, C = {C}")
            logging.info(f" angleC = {angleC}, angleBC = {angleA}, angleCA = {angleB}")

        t = turtle.Turtle()
        t.pencolor(self.triangle.generate_random_rgb_color())
        t.width(random.randint(1, 10))

        t.speed(0)
        t.right(random.randint(0, 359)) # Random initial direction
        t.forward(A)
        t.left(180 - angleC) # 180 - angle = outer angle
        t.forward(B)
        t.left(180 - angleA)
        t.forward(C)
        t.left(180 - angleB)
        t.hideturtle()

    def onLeftClick(self, x, y):
        if self.debug: logging.info("Left click, drawing new triangle")
        self.draw_triangle()
        self.bind_events()

    def onRightClick(self, x, y):
        if self.debug: logging.info("Right click, clearing canvas and drawing new triangle")
        self.screen.clear()
        self.screen.bgcolor("white")
        self.draw_instructions()
        self.draw_triangle()
        self.bind_events()

    def on_close(self):
        if self.debug: logging.info("Closing turtle")
        turtle.bye()

    def bind_events(self):
        self.screen.onclick(self.onLeftClick, btn=1)
        self.screen.onclick(self.onRightClick, btn=3)
        self.screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", self.on_close)

    def draw_turtle_triangle(self, debug=False):
        self.debug = debug
        self.screen = turtle.Screen()
        self.screen.bgcolor("white")
        self.screen.title("Random Triangle")
        self.screen.setup(800, 600)

        if self.debug: logging.info("Screen initialized, drawing first triangle...")

        self.draw_triangle()
        self.draw_instructions()
        self.bind_events()

        self.screen.listen()
        self.screen.mainloop()
