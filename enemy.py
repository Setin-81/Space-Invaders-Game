import turtle
import random
import math

class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(["#ff4c4c", "#ffcc00", "#00ffcc", "#66ff33", "#ff33cc"]))
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.start_x = random.randint(-200, 200)
        self.setposition(self.start_x, random.randint(100, 250))
        self.wobble_angle = random.uniform(0, math.pi * 2)
        self.amplitude = random.randint(5, 20)
        self.size_direction = 1
        self.current_size = 1.0

    def move_wobble(self, base_speed):
        """Move enemy in a sine wave pattern with pulsing size."""
        self.wobble_angle += 0.05
        x_offset = math.sin(self.wobble_angle) * self.amplitude
        self.setx(self.start_x + x_offset)

        # Pulse effect
        self.current_size += 0.02 * self.size_direction
        if self.current_size >= 1.3 or self.current_size <= 0.9:
            self.size_direction *= -1
        self.shapesize(self.current_size, self.current_size)
