import pygame as pg
pg.init()
screen = pg.display.set_mode((700,500))
color = (250,250,250)
screen.fill(color)
x = 0
clock = pg.time.Clock()
#pg.draw.circle(screen,'red',(350,250),100)
#pg.draw.line(screen,'black',(0,50,),(700,50),width=1)
#pg.draw.polygon(screen,'green',[(0,500),(350,0),(700,500)])

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    x +=1
    if x >700:
        x = 0
    pg.draw.rect(screen,'blue',(x,200,50,50))
    pg.display.update()
    screen.fill(color)
    clock.tick(800)