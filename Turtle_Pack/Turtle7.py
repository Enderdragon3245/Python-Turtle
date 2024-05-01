import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
forw = 1
n = 70
h = 70
while True:
    t.forward(forw)
    t.left(120)
    t.left(1)
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    forw += 1

