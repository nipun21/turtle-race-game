#turtle Game
from turtle import *
from random import randint
speed(10)
penup()
goto(-320,160)
for step in range(16):
    write(step)
    forward(20)
    right(90)
    forward(10)
    pendown()
    forward(150)
    pendown()
    backward(160)
    left(90)
    forward(20)
    
rad = Turtle()
rad.color('red')
rad.shape('turtle')
rad.penup()
rad.goto(-320,140)
rad.pendown()

bla = Turtle()
bla.color('blue')
bla.shape('turtle')
bla.penup()
bla.goto(-320,110)
bla.pendown()

blk = Turtle()
blk.color('black')
blk.shape('turtle')
blk.penup()
blk.goto(-320,80)
blk.pendown()


grn = Turtle()
grn.color('green')
grn.shape('turtle')
grn.penup()
grn.goto(-320,50)
grn.pendown()
for trn in range(205):
    rad.forward(randint(1,5))
    bla.forward(randint(1,5))
    blk.forward(randint(1,5))
    grn.forward(randint(1,5))
