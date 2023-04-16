import random

import turtle

import pygame

# Set up Pygame for sound effects

pygame.mixer.init()

wing_sound = pygame.mixer.Sound("wing.wav")

hit_sound = pygame.mixer.Sound("hit.wav")

point_sound = pygame.mixer.Sound("point.wav")

# Set up the game window

win = turtle.Screen()

win.title("Flappy Bird")

win.bgcolor("white")

win.setup(width=500, height=600)

# Set up the bird sprite

bird = turtle.Turtle()

bird.shape("circle")

bird.color("yellow")

bird.penup()

bird.speed(0)

bird.goto(-200, 0)

bird.dy = 0

# Set up the pipes

pipes = []

for i in range(3):

    pipe_top = turtle.Turtle()

    pipe_top.shape("square")

    pipe_top.color("green")

    pipe_top.penup()

    pipe_top.speed(0)

    pipe_top.goto(300 + i * 200, 200)

    pipe_top.dx = -2

    pipe_bottom = turtle.Turtle()

    pipe_bottom.shape("square")

    pipe_bottom.color("green")

    pipe_bottom.penup()

    pipe_bottom.speed(0)

    pipe_bottom.goto(300 + i * 200, -200)

    pipe_bottom.dx = -2

    pipes.append((pipe_top, pipe_bottom))

# Set up the score

score = 0

score_text = turtle.Turtle()

score_text.color("black")

score_text.penup()

score_text.hideturtle()

score_text.goto(0, 260)

score_text.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Set up the game over screen

game_over_text = turtle.Turtle()

game_over_text.color("black")

game_over_text.penup()

game_over_text.hideturtle()

game_over_text.goto(0, 100)

game_over_text.write("Game Over", align="center", font=("Courier", 36, "normal"))

game_over_text2 = turtle.Turtle()

game_over_text2.color("black")

game_over_text2.penup()

game_over_text2.hideturtle()

game_over_text2.goto(0, 50)

game_over_text2.write("Press 'r' to restart", align="center", font=("Courier", 24, "normal"))

# Set up the difficulty levels

difficulties = [

    ("Easy", 2),

    ("Medium", 4),

    ("Hard", 6),

]

current_difficulty = 0

# Set up the game state

game_over = False

# Function to move the bird up

def move_up():

    if not game_over:

        bird.dy = 6

        wing_sound.play()

# Function to restart the game

def restart():

    global score, current_difficulty, game_over

    score = 0

    score_text.clear()

    score_text.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    current_difficulty = 0

    for pipe_top, pipe_bottom in pipes:

        pipe_top.goto(pipe_top.xcor(), 200)

        pipe_bottom.goto(pipe_bottom.xcor(), -200)

        pipe_top.dx = -difficulties[current_difficulty][1]

        pipe_bottom.dx = -difficulties[current_difficulty][1]

    bird.goto(-200, 0)

    bird.dy = 0

    game_over_text.clear()

    game_over_text2.clear()

    game_over = False
Set up the keyboard bindings

win.listen()

win.onkeypress(move_up, "space")

win.onkeypress(restart, "r")

Main game loop

while True:

# Move the bird

bird.dy -= 0.2

bird.sety(bird.ycor() + bird.dy)
# Move the pipes

for pipe_top, pipe_bottom in pipes:

    pipe_top.setx(pipe_top.xcor() + pipe_top.dx)

    pipe_bottom.setx(pipe_bottom.xcor() + pipe_bottom.dx)

    # Check for collision with the bird

    if (bird.xcor() > pipe_top.xcor() - 20 and bird.xcor() < pipe_top.xcor() + 20) and (bird.ycor() > pipe_top.ycor() - 150 or bird.ycor() < pipe_bottom.ycor() + 150):

        hit_sound.play()

        game_over = True

    # Check for scoring

    if bird.xcor() > pipe_top.xcor() and bird.xcor() < pipe_top.xcor() + pipe_top.dx:

        score += 1

        score_text.clear()

        score_text.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

        point_sound.play()

    # Check for pipes going off the screen

    if pipe_top.xcor() < -250:

        pipe_top.goto(250, random.randint(100, 250))

        pipe_bottom.goto(250, random.randint(-250, -100))

        current_difficulty = min(current_difficulty + 1, len(difficulties) - 1)

        pipe_top.dx = -difficulties[current_difficulty][1]

        pipe_bottom.dx = -difficulties[current_difficulty][1]

# Check for bird going off the screen

if bird.ycor() < -300:

    hit_sound.play()

    game_over = True

# Check for game over

if game_over:

    game_over_text.showturtle()

    game_over_text2.showturtle()

# Update the screen

win.update()




