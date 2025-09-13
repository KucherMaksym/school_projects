import tkinter as tk
import random
import math
from triangle_utils import TriangleUtils

class TkinterDrawer:
    def __init__(self):
        self.triangle = TriangleUtils()
        self.root = None
        self.canvas = None
        self.app_width = 1920
        self.app_height = 1080

    def draw_triangle(self):
        # Calculate coordinates of triangle vertices
        offset = (random.randint(-300, 300), random.randint(-300, 300))

        A, B, C, angleA, angleB, angleC = self.triangle.generate_random_triangle()

        print(f" A = {A}, B = {B}, C = {C}")
        print(f" angleC = {angleC}, angleBC = {angleA}, angleCA = {angleB}")

        A_coordinates = (self.app_width / 2 + offset[0], self.app_height / 2 + offset[1])
        B_coordinates = (A_coordinates[0] + C + offset[0], A_coordinates[1] + offset[1])

        # Calculate coordinates of triangle vertices
        Cx = A_coordinates[0] + B * math.cos(math.radians(angleA))
        Cy = A_coordinates[1] - B * math.sin(math.radians(angleA))
        C_coordinates = (Cx, Cy)

        # Generate random color and width
        color = self.triangle.generate_random_rgb_color()
        width = random.randint(1, 10)

        # Draw triangle
        self.canvas.create_line(
            A_coordinates[0], A_coordinates[1],
            B_coordinates[0], B_coordinates[1],
            width=width, fill=color
        )
        self.canvas.create_line(
            B_coordinates[0], B_coordinates[1],
            C_coordinates[0], C_coordinates[1],
            width=width, fill=color
        )
        self.canvas.create_line(
            C_coordinates[0], C_coordinates[1],
            A_coordinates[0], A_coordinates[1],
            width=width, fill=color
        )

    def on_left_click(self, event):
        self.draw_triangle()

    def on_right_click(self, event):
        self.canvas.delete("all")
        self.canvas.configure(bg="white")
        self.draw_triangle()

    def bind_events(self):
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.focus_set()

    def draw_tkinter_triangle(self):
        self.root = tk.Tk()
        self.root.title('Random Triangle')
        self.root.geometry(f"{self.app_width}x{self.app_height}")

        self.canvas = tk.Canvas(
            self.root,
            width=self.app_width,
            height=self.app_height,
            bg='white'
        )
        self.canvas.pack(anchor="center", expand=True)

        self.draw_triangle()
        self.bind_events()

        instructions = "Left mouse button - new triangle | Right mouse click - clear and draw a new triangle"
        self.canvas.create_text(
            10, 10,
            text=instructions,
            anchor="nw",
            fill="black",
            font=("Arial", 12)
        )

        self.root.mainloop()