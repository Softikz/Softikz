import pygame as pg
pg.init()
screen = pg.display.set_mode((700,500))
color = (250,250,250)
screen.fill(color)

x = 0
n = 10
size = 700
for i in range(n):
    pg.draw.rect(screen, 'black', (x, 0, size//n, 500))
    x += size//n*2


pg.display.update()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False