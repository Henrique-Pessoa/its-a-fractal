import numpy as np
import turtle as t
import colorsys as cs
#t.Screen().bgcolor(i,j,b)
t.setup(1080,980)
t.speed(0)
t.tracer(10)
t.width(2)
t.bgcolor("black")
n = 36
h = 0
p = 0


for j in range(2000000):
    for i in range(2000000):
        color = cs.hsv_to_rgb(h,1,1)
        h+=1/6
        j+=1
        if(p == 1):
            c = "black"
            p = 0
        else:
            c = "white"
            p = 1
        t.color(color)
        t.circle(350)
        t.left(50)
        t.circle(j)
        t.right(4)
        t.circle(1,1)
        print(j)
        if j == 1000:
            t.done()
