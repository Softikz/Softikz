from tkinter import *
import random

WIDTH = 900
HEIGHT = 300

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 150

BALL_SPEED_MULTIPLIER = 1.05
BALL_MAX_SPEED = 40
BALL_SIZE = 30

BALL_SPEED_X = 20
BALL_SPEED_Y = BALL_SPEED_X
BALL_VELOCITY_Y = BALL_SPEED_X

LEFT_SCORE = 0
RIGHT_SCORE = 0

RIGHT_PADDLE_X = WIDTH - PADDLE_WIDTH

def update_score(side):
    global LEFT_SCORE, RIGHT_SCORE
    if side == "right":
        RIGHT_SCORE += 1
        canvas.itemconfig(right_score_text, text=RIGHT_SCORE)
    else:
        LEFT_SCORE += 1
        canvas.itemconfig(left_score_text, text=LEFT_SCORE)

def reset_ball():
    global BALL_SPEED_X
    canvas.coords(ball, WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, WIDTH / 2 + BALL_SIZE / 2, HEIGHT / 2 + BALL_SIZE / 2)
    BALL_SPEED_X = -(BALL_SPEED_X * -BALL_SPEED_Y) / abs(BALL_SPEED_X)

def change_ball_direction(direction):
    global BALL_SPEED_X, BALL_VELOCITY_Y
    if direction == "strike":
        BALL_VELOCITY_Y = random.randrange(-10, 10)
        if abs(BALL_SPEED_X) < BALL_MAX_SPEED:
            BALL_SPEED_X *= -BALL_SPEED_MULTIPLIER
        else:
            BALL_SPEED_X = -BALL_SPEED_X
    else:
        BALL_VELOCITY_Y = -BALL_VELOCITY_Y

root = Tk()

canvas = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
canvas.pack()

canvas.create_line(PADDLE_WIDTH, 0, PADDLE_WIDTH, HEIGHT, fill="black")
canvas.create_line(WIDTH - PADDLE_WIDTH, 0, WIDTH - PADDLE_WIDTH, HEIGHT, fill="black")
canvas.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="black")

ball = canvas.create_oval(WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, WIDTH / 2 + BALL_SIZE / 2, HEIGHT / 2 + BALL_SIZE / 2, fill="green")
left_paddle = canvas.create_line(PADDLE_WIDTH / 2, 0, PADDLE_WIDTH / 2, PADDLE_HEIGHT, width=PADDLE_WIDTH, fill="red")
right_paddle = canvas.create_line(WIDTH - PADDLE_WIDTH / 2, 0, WIDTH - PADDLE_WIDTH / 2, PADDLE_HEIGHT, width=PADDLE_WIDTH, fill="blue")

right_score_text = canvas.create_text(WIDTH - WIDTH / 6, PADDLE_HEIGHT / 4, text=RIGHT_SCORE, font="Arial 20", fill="white")
left_score_text = canvas.create_text(WIDTH / 6, PADDLE_HEIGHT / 4, text=LEFT_SCORE, font="Arial 20", fill="white")

PADDLE_SPEED = 20
right_paddle_velocity = 0
left_paddle_velocity = 0

AI_PADDLE_SPEED = 20
AI_PADDLE_X = 0
AI_PADDLE_Y = 0
