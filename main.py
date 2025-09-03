import turtle
import math
import random
import time
import sys

try:
    import winsound
    sound_on = True
except:
    sound_on = False

from player import Player
from bullet import Bullet
from enemy import Enemy

# --- Screen setup ---
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders - Beautiful Edition")
wn.setup(width=800, height=600)
wn.tracer(0)

# Draw stars in background
def draw_stars():
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.color("white")
    for _ in range(50):
        star.penup()
        star.goto(random.randint(-390, 390), random.randint(-290, 290))
        star.dot(random.randint(2, 4))

draw_stars()

# --- Create game objects ---
player = Player()
bullet = Bullet()
number_of_enemies = 6
enemies = [Enemy() for _ in range(number_of_enemies)]
enemy_speed = 0.8

# Explosion turtle
explosion = turtle.Turtle()
explosion.shape("circle")
explosion.penup()
explosion.hideturtle()

# --- Score & Timer ---
score = 0
level = 1
game_time = 60
start_time = time.time()

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-380, 260)
score_pen.hideturtle()

# --- Controls ---
wn.listen()
wn.onkey(player.move_left, "Left")
wn.onkey(player.move_right, "Right")
wn.onkey(lambda: fire_bullet(), "space")

def fire_bullet():
    if bullet.state == "ready":
        bullet.fire(player.xcor(), player.ycor())
        if sound_on:
            winsound.PlaySound("shoot.wav", winsound.SND_ASYNC)

def update_score():
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(game_time - elapsed_time, 0)
    score_pen.clear()
    score_pen.write(f"Score: {score}   Level: {level}   Time: {remaining_time}s",
                    False, align="left", font=("Arial", 14, "normal"))
    if remaining_time <= 0:
        game_over()

def is_collision(t1, t2):
    return math.dist([t1.xcor(), t1.ycor()], [t2.xcor(), t2.ycor()]) < 20

def game_over():
    global running
    running = False
    player.hideturtle()
    for enemy in enemies:
        enemy.hideturtle()
    turtle.clearscreen()
    wn.bgcolor("black")
    wn.title("GAME OVER")
    over_text = turtle.Turtle()
    over_text.color("white")
    over_text.write(f"GAME OVER\nFinal Score: {score}", align="center", font=("Arial", 24, "bold"))
    time.sleep(3)
    sys.exit()

def rainbow_explosion(x, y):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for c in colors:
        explosion.color(c)
        explosion.setposition(x, y)
        explosion.shapesize(1.5, 1.5)
        explosion.showturtle()
        wn.update()
        time.sleep(0.05)
    explosion.hideturtle()

# --- Main Loop ---
running = True
while running:
    wn.update()
    update_score()

    # Move enemies
    for enemy in enemies:
        enemy.move_wobble(enemy_speed)

        # Collision with bullet
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet.state = "ready"
            bullet.setposition(0, -400)
            rainbow_explosion(enemy.xcor(), enemy.ycor())
            enemy.setposition(random.randint(-200, 200), random.randint(100, 250))
            score += 10
            if sound_on:
                winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

            if score % 50 == 0:
                level += 1
                enemy_speed += 0.2

        # Collision with player
        if is_collision(enemy, player) or enemy.ycor() < -250:
            game_over()

    # Move bullet
    bullet.move()

    time.sleep(0.02)
