import pygame as pg
pg.init()
screen = pg.display.set_mode((700,500))
color = (250,250,250)
screen.fill(color)
pg.draw.line(screen,'black',(0,0),(700,500),width=50)
pg.draw.line(screen,'black',(700,0),(0,500),width=50)
pg.display.update()
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False