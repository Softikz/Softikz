from turtle import *

bgcolor('black')
color('red', 'yellow')
speed(0)


for k in range(200):
 begin_fill()
 forward(300 - k)
 left(170)
 forward(300 - k)
 end_fill()

done()