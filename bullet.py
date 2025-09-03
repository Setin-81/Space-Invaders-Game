import turtle

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("#ffff66")
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=0.8)
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.hideturtle()
        self.speed_value = 15
        self.state = "ready"
        self.trail = []

    def fire(self, x, y):
        if self.state == "ready":
            self.state = "fire"
            self.setposition(x, y + 10)
            self.showturtle()

    def move(self):
        if self.state == "fire":
            self.sety(self.ycor() + self.speed_value)

            # Create a small trail dot
            trail_dot = turtle.Turtle()
            trail_dot.shape("circle")
            trail_dot.color("#ffffcc")
            trail_dot.shapesize(0.1, 0.1)
            trail_dot.penup()
            trail_dot.goto(self.xcor(), self.ycor() - 5)
            self.trail.append(trail_dot)

            # Remove oldest trail piece
            if len(self.trail) > 5:
                t = self.trail.pop(0)
                t.hideturtle()

        if self.ycor() > 275:
            self.hideturtle()
            self.state = "ready"
            for t in self.trail:
                t.hideturtle()
            self.trail.clear()
