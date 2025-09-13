import random
import math

class TriangleUtils:
    def generate_random_rgb_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f'#{r:02x}{g:02x}{b:02x}'

    def generate_random_triangle(self):
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
        return A, B, C, angleA, angleB, angleC
