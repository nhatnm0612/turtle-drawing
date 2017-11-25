from turtle import *


def flower(turColor, turNum, turRange, startAngle = 0):
    for i in range(turNum):
        Tur = Turtle()
        Tur.setheading(startAngle)
        Tur.shape("turtle")
        Tur.color(turColor)
        Tur.speed(0)
        Tur.up()
        Tur.right(360*i/turNum)
        Tur.forward(turRange)
        Tur.down()
        Tur.begin_fill()
        Tur.right(180/turNum)
        Tur.forward(turRange)
        Tur.left(360/turNum)
        Tur.forward(turRange)
        Tur.left(180 - 360/turNum)
        Tur.forward(turRange)
        Tur.left(360/turNum)
        Tur.forward(turRange)
        Tur.end_fill()
        


Scr = Screen()
Scr.bgcolor("black")

flower("midnightblue", 10, 50)
flower("blueviolet", 10, 50, 18)
flower("steelblue", 10, 75)
flower("darkgrey", 10, 75, 18)

Scr.mainloop()
