import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)
        self.speed_value = 12

    def move_left(self):
        x = self.xcor() - self.speed_value
        if x < -380:
            x = -380
        self.setx(x)

    def move_right(self):
        x = self.xcor() + self.speed_value
        if x > 380:
            x = 380
        self.setx(x)
