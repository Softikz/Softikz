import  pygame as pg
import random

pg.init()

WIDTH = 700
HEIGHT = 700

left_player= pg.Rect(30,350 , 20, 100)
right_player= pg.Rect(670, 350, 20, 100)

ball=pg.Rect(350,350,10,10)

screen = pg.display.set_mode((WIDTH,HEIGHT))
color = (255,255,255)

speed_platform = 10
speed_ball_x= random.randint(3,5)
speed_ball_y= random.randint(3,5)

clock = pg.time.Clock()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()

    if keys[pg.K_w] and left_player.top > 0 :
        left_player.y -= speed_platform
    if keys[pg.K_s] and left_player.bottom < 700:
        left_player.y += speed_platform

    if keys[pg.K_i] and right_player.top > 0 :
        right_player.y -= speed_platform
    if keys[pg.K_k] and right_player.bottom < 700:
        right_player.y += speed_platform

    ball.x += speed_ball_x
    ball.y += speed_ball_y

    if ball.colliderect(right_player) or ball.colliderect(left_player):
        speed_ball_x = -speed_ball_x

    if ball.x >700:
        ball.y = 350
        ball.x = 350
    if ball.x < 0 :
        ball.y = 350
        ball.x = 350
    if ball.y >700 or ball.y < 0 :
        speed_ball_y = -speed_ball_y

    screen.fill('white')
    pg.draw.rect(screen, 'black', left_player)
    pg.draw.rect(screen, 'black', right_player)
    pg.draw.ellipse(screen,'black',ball)
    pg.display.update()
    clock.tick(60)